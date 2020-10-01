from datetime import datetime
from global_data import channels, messages
from helper_functions import user_in_channel, get_u_id
from error import InputError, AccessError

def message_send(token, channel_id, message):


    if (len(message) >= 1000):
        raise InputError("Message too long")
        
    if (user_in_channel(get_u_id(token), channel_id) == False):
        raise AccessError("User not in channel")
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
     
    new_message = {
        'message_id': len(messages) + 1,
        'u_id': get_u_id(token),
        'message': message,
        'time_created': timestamp,
    }
    
    messages.append(new_message['message_id'])

    for channel in channels:
        if (channel['channel_id'] == channel_id):
            channel['messages'].append(new_message)
            break
    
    
    return {
        'message_id': 1,
    }

def message_remove(token, message_id):
    return {
    }

def message_edit(token, message_id, message):
    return {
    }
