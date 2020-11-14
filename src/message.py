'''
File of message funtions, message_send, message_remove and message edit
'''
from datetime import datetime
from global_data import channels, messages
from helper_functions import user_in_channel, get_u_id, message_exists, \
user_is_owner, message_creator, find_channel, permission, \
user_in_channel, channel_exists
from error import InputError, AccessError
from threading import Timer

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

def message_sendlater(token, channel_id, message, time_sent):
    # Error handling for long messages, non-existent channels, invalid time
    # and user not part of channel
    if len(message) > 1000:
        raise InputError("Message is too long")

    if not channel_exists(channel_id):
        raise InputError("Channel cannot be found")

    now = datetime.now()
    if time_sent < datetime.timestamp(now):
        raise InputError("Requested time to send message has already passed")

    if not user_in_channel(get_u_id(token), channel_id):
        raise AccessError("User is not part of the requested channel")

    m_id = 1
    # Calculating message_id
    for channel in channels:
        for message in channel['messages']:
            m_id = m_id + 1

    # Calculating time difference and 
    delay = time_sent - datetime.timestamp(now)

    # Starting timer to execute sending the message
    t = Timer(delay, message_sendlater_action, args=[get_u_id(token), m_id, message, time_sent, channel_id])
    t.start()

    return {'message_id' : m_id}

def message_sendlater_action(u_id, m_id, message, time_sent, channel_id):   
    new_message = {
        'message_id' : m_id,
        'u_id' : u_id,
        'creator' : u_id,
        'message' : message,
        'time_created' : time_sent,
        'reacts' : [],
        'is_pinned' : False
    }

    for channel in channels:
        if channel['channel_id'] == channel_id:
            channel['messages'].append(new_message)
            break

