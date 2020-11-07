'''
File of message funtions, message_send, message_remove and message edit
'''
from datetime import datetime
from global_data import channels, messages
from helper_functions import user_in_channel, get_u_id, message_exists, \
user_is_owner, message_creator, find_channel, getChannelData, saveChannelData, \
permission, user_a_member_persist
from error import InputError, AccessError

def message_send(token, channel_id, message):
    '''
    Function sends message to channel
    '''
    channel_id = int(channel_id)

    #check message length
    if len(message) > 1000:
        raise InputError("Message too long")
    #check user send message is in the channel
    if not user_in_channel(get_u_id(token), channel_id):
        raise AccessError("User not in channel")

    #creating timestamp for message
    now = datetime.now()
    timestamp = datetime.timestamp(now)

    m_id = len(messages) + 1

    #creating new message dictionary
    new_message = {
        'message_id':m_id,
        'u_id': get_u_id(token),
        'creator':  get_u_id(token),
        'message': message,
        'time_created': timestamp,
    }
    #adding message_id to list
    messages.append(new_message['message_id'])

    #appending new message to message list in channel dictionary
    for channel in channels:
        if channel['channel_id'] == channel_id:
            channel['messages'].append(new_message)
            break

    return {
        'message_id': m_id,
    }

def message_remove(token, message_id):
    '''
    Funtion remove message from channel given message and token
    '''
    u_id = get_u_id(token)

    channel_id = find_channel(message_id)

    m_id = message_exists(message_id)
    owner = user_is_owner(u_id, channel_id)
    creator = message_creator(u_id, message_id)
    permission_id = permission(u_id)

    #raising error if message doesnt exist
    if not m_id:
        raise InputError("Invalid message ID")
    #checking if user has authorization to remove message
    if not creator and not owner and permission_id == 2:
        raise AccessError("user is not authorised to remove message")
    #removing message from channel
    for channel in channels:
        for chan_messages in channel['messages']:
            if chan_messages['message_id'] == message_id:
                channel['messages'].remove(chan_messages)
                return {}
    return {}

def message_edit(token, message_id, message):
    '''
    Function edits message with new message given
    '''
    u_id = get_u_id(token)

    channel_id = find_channel(message_id)

    owner = user_is_owner(u_id, channel_id)
    creator = message_creator(u_id, message_id)
    permission_id = permission(u_id)

    #checking if user has authorization to edit message
    if not creator and not owner and permission_id == 2:
        raise AccessError("user is not authorised to remove message")

    #checking if new message is empty strin
    no_message = False
    if message == "":
        no_message = True

    for channel in channels:
        for chan_messages in channel['messages']:
            if chan_messages['message_id'] == message_id:
                #removing message if empty string
                if no_message:
                    channel['messages'].remove(chan_messages)
                #chaning old message to new message
                else:
                    chan_messages['message'] = message

    return {}

def message_react(token, message_id, react_id):
    '''
    Adds a 'react' to a certain message within a channel the authorised user
    has joined
    '''
    channel_id = 0
    the_message = {}
    react_exists = False
    # Raising error if message not found
    if not message_exists(message_id):
        raise InputError("Message cannot be found in any channel")

    channel_data = getChannelData()
    channel_list = channel_data['channels']
    # Obtaining channel id as well as the message dictionary
    for channel in channel_list:
        for message in channel['messages']:
            if message['message_id'] == message_id:
                channel_id = channel['channel_id']
                the_message = message
                break

    # Getting user_id, and seeing if the user is a member of the channel
    the_user = get_u_id(token)
    if not user_a_member_persist(the_user, channel_id):
        raise InputError("User is not a member of the message's channel")

    # Error returned if react_id is invalid
    if react_id != 1:
        raise InputError("React_id is not valid")

    message_reacts = the_message['reacts']
    reacted_users = []

    for react in message_reacts:
        if react['react_id'] == react_id:
            reacted_users = react['u_ids']
            break

    # Error returned if user has already used the react for the message
    for user in reacted_users:
        if user == the_user:
            raise InputError("User has already used this react for this message")

    # Find the react in channel message and add in the user to people who've reacted
    for channel in channel_list:
        if channel['channel_id'] == channel_id:
            for message in channel['messages']:
                if message['message_id'] == message_id:
                    for react in message['reacts']:
                        if react['react_id'] == react_id:
                            react['u_ids'].append(the_user)
                            react_exists = True
                            break
                    # If react doesn't yet exist for that message add it in
                    if not react_exists:
                        message['reacts'].append({react_id}, [the_user], True)
                    break
            break

    saveChannelData(channel_list)
    return {}

def message_unreact(token, message_id, react_id):
    '''
    Removes a 'react' to a certain message within a channel the authorised user
    has joined
    '''
    channel_id = 0
    the_message = {}
    react_found = False
    # Raising error if message not found
    if not message_exists(message_id):
        raise InputError("Message cannot be found in any channel")

    channel_data = getChannelData()
    channel_list = channel_data['channels']
    # Obtaining channel id as well as the message dictionary
    for channel in channel_list:
        for message in channel['messages']:
            if message['message_id'] == message_id:
                channel_id = channel['channel_id']
                the_message = message
                break

    # Getting user_id, and seeing if the user is a member of the channel
    the_user = get_u_id(token)
    if not user_a_member_persist(the_user, channel_id):
        raise InputError("User is not a member of the message's channel")

    # Error returned if react_id is invalid
    if react_id != 1:
        raise InputError("React_id is not valid")

    for react in the_message['reacts']:
        if react_id == react['react_id']:
            react_found = True
            break
    # Error is returned if no reacts of the specified react_id is found in msg
    if react_found == False:
        raise InputError("Message does not contain a react of that react_id")

    # Find react_id and remove user from the users who have used that react
    for channel in channel_list:
        if channel['channel_id'] == channel_id:
            for message in channel['messages']:
                if message['message_id'] == message_id:
                    for react in message['reacts']:
                        if react['react_id'] == react_id:
                            react['u_ids'].remove(the_user)
                            # If there are no more users who have used the react
                            # remove it completely from the message
                            if len(react['u_ids']) == 0:
                                message['reacts'].remove(react)
                            break

                    break
            break

    saveChannelData(channel_list)
    return {}
