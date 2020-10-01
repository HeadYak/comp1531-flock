from global_data import channels, users
import pytest
from error import InputError
from helper_functions import get_u_id
from helper_functions import create_member
def channels_list(token):
    return {
        'channels': [
        	{
        		'channel_id': 1,
        		'name': 'My Channel',
        	}
        ],
    }

def channels_listall(token):
    return {
        'channels': [
        	{
        		'channel_id': 1,
        		'name': 'My Channel',
        	}
        ],
    }

def channels_create(token, name, is_public):
    print(token)
    print(users)
    valid_token = False
    for user in users:
        if(user['token'] == token):
            valid_token = True
    if(valid_token == True and len(name) <= 20):
        
        new_channel = {
            'channel_id': len(channels)+1,
            'name': name,
            'is_public': is_public,
            'creator': create_member(get_u_id(token)),
            'owners': [create_member(get_u_id(token))],
            'members': [create_member(get_u_id(token))],
            'messages': []
        }
        new_channel_copy = new_channel.copy()
        channels.append(new_channel_copy)

        return {
            'channel_id': new_channel_copy['channel_id']
        }
        
    if(len(name) > 20):
        raise InputError('Invalid Name')

