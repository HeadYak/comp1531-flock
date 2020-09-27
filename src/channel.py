from global_data import users, channels
import pytest
from error import InputError
from helper_functions import user_in_channel, user_exists, channel_exists, create_member, get_u_id


def channel_invite(token, channel_id, u_id):
    
    
    if channel_exists(channel_id) == False:
        raise InputError('Invalid channel')
        
    elif user_exists(u_id) == False:
        raise InputError('Invalid user id')
    
    authorised_u_id == get_u_id(token)
    
    elif user_in_channel(authorised_u_id, channel_id) == False:
        raise InputError('User not a member of channel')
       
    else:
        for channel in channels:
            if channel['channel_id'] == channel_id:
                channel['members'].append(create_member(u_id))   
    
    return {}

def channel_details(token, channel_id):
    return {
        'name': 'Hayden',
        'owner_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
        'all_members': [
            {
                'u_id': 1,
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
            }
        ],
    }

def channel_messages(token, channel_id, start):
    return {
        'messages': [
            {
                'message_id': 1,
                'u_id': 1,
                'message': 'Hello world',
                'time_created': 1582426789,
            }
        ],
        'start': 0,
        'end': 50,
    }

def channel_leave(token, channel_id):

     if channel_exists(channel_id) == False:
        raise InputError('Invalid channel')
    
    authorised_u_id == get_u_id(token)
    
    elif user_in_channel(authorised_u_id, channel_id) == False:
        raise InputError('User not a member of channel')
    
    else:
        for channel in channels:
            if channel['channel_id'] == channel_id:
                for member in channel['members']:
                    if member['u_id'] == u_id:
                       channel['members']. remove(member)
    
    return {}

def channel_join(token, channel_id):
    
    u_id == get_u_id(token)
    
    public = False 
    for channel in channels:
        if channel['channel_id'] == channel_id:
            if channel['is_public'] == True:
                public = True
    
    if public == False:
        raise InputError('Private Channel')
    
    elif channel_exists(channel_id) == False:
        raise InputError('Invalid channel')
    
    else:
        for channel in channels:
            if channel['channel_id'] == channel_id:
                channel['members'].append(create_member(u_id))   
        
    return {}

def channel_addowner(token, channel_id, u_id):
    return {
    }

def channel_removeowner(token, channel_id, u_id):
    return {
    }
