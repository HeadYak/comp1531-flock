'''
File of message funtions, message_send, message_remove and message edit
'''
from datetime import datetime
from global_data import channels, messages
from helper_functions import user_in_channel, get_u_id, message_exists, \
user_is_owner, message_creator, find_channel
from error import InputError, AccessError

def message_send(token, channel_id, message):
    '''
    Function sends message to channel
    '''
    if len(message) > 1000:
        raise InputError("Message too long")
    if not user_in_channel(get_u_id(token), channel_id):
        raise AccessError("User not in channel")

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    m_id = len(messages) + 1

    new_message = {
        'message_id':m_id,
        'u_id': get_u_id(token),
        'creator':  get_u_id(token),
        'message': message,
        'time_created': timestamp,
    }
    messages.append(new_message['message_id'])

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

    if not m_id:
        raise InputError("Invalid message ID")
    if not creator and not owner:
        raise AccessError("user is not authorised to remove message")
    for channel in channels:
        for chan_messages in channel['messages']:
            if chan_messages['message_id'] == message_id:
                channel['messages'].remove(chan_messages)
                return
    return

def message_edit(token, message_id, message):
    '''
    Function edits message with new message given
    '''
    u_id = get_u_id(token)

    channel_id = find_channel(message_id)

    owner = user_is_owner(u_id, channel_id)
    creator = message_creator(u_id, message_id)

    if not creator and not owner:
        raise AccessError("user is not authorised to remove message")

    no_message = False
    if message == "":
        no_message = True

    for channel in channels:
        for chan_messages in channel['messages']:
            if chan_messages['message_id'] == message_id:
                if no_message:
                    channel['messages'].remove(chan_messages)
                else:
                    chan_messages['message'] = message

    return {}
