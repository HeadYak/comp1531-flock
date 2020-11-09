'''
File of message funtions, message_send, message_remove and message edit
'''
from datetime import datetime
from global_data import channels, messages
from helper_functions import user_in_channel, get_u_id, message_exists, \
user_is_owner, message_creator, find_channel, getChannelData, permission
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
        'is_pinned': False
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
    
def message_pin(token, message_id):
    '''
    Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
    '''
    u_id = get_u_id(token)

    channel_id = find_channel(message_id)
    message = find_message(channel_id)

    m_id = message_exists(message_id)
    auth_user = user_in_channel(u_id, channel_id)
    
    is_pinned = False

    # Input errors for invalid / already pinned messages
    if not m_id:
        raise InputError("Invalid message ID")
    if message['is_pinned'] == True:
        raise InputError("Message is already pinned")
    # Access error for non-owners / unauthorised users
    if not auth_user:
        raise AccessError("User is not a member of the channel")

    for unpinned_message in message['is_pinned']:
        message['is_pinned'] = True
    
    return {}
    
def message_unpin(token, message_id):
    '''
    Given a message within a channel, remove its mark as unpinned
    '''
    u_id = get_u_id(token)

    channel_id = find_channel(message_id)
    message = find_message(channel_id)

    m_id = message_exists(message_id)
    auth_user = user_in_channel(u_id, channel_id)

    is_pinned = True

    # Input errors for invalid / already unpinned messages
    if not m_id:
        raise InputError("Invalid message ID")
    if message['is_pinned'] == False:
        raise InputError("Message is already unpinned")
    # Access error for non-owners / unauthorised users
    if not auth_user:
        raise AccessError("User is not a member of the channel")
    
    for pinned_message in message['is_pinned']:
        message['is_pinned'] = False
        
    return {}
