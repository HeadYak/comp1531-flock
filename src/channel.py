from global_data import users, channels
import pytest
from error import InputError, AccessError
from helper_functions import user_in_channel, user_exists, channel_exists, create_member, get_u_id, get_token, user_is_owner, user_is_creator


def channel_invite(token, channel_id, u_id):
    
    authorised_u_id = get_u_id(token)
    
    if (channel_exists(channel_id) == False):
        raise InputError('Invalid channel')
        
    if(user_exists(u_id) == False):
        raise InputError('Invalid user id')
    
    if (user_in_channel(authorised_u_id, channel_id) == False):
        raise InputError('User not a member of channel')
    
    for channel in channels:
        if (channel['channel_id'] == channel_id):
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

    authorised_u_id = get_u_id(token)

    if (channel_exists(channel_id) == False):
        raise InputError('Invalid channel')
    
    if (user_in_channel(authorised_u_id, channel_id) == False):
        raise InputError('User not a member of channel')

    for channel in channels:
        if (channel['channel_id'] == channel_id):
            for member in channel['members']:
                print(channel['members'])
                if (member['u_id'] == authorised_u_id):
                    print(channel['members'])
                    channel['members']. remove(member)
                    print(channel['members'])
    
    return {}

def channel_join(token, channel_id):
    
    u_id = get_u_id(token)
    
    public = False 
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            if (channel['is_public'] == True):
                public = True
    
    if (public == False):
        raise InputError('Private Channel')
    
    if (channel_exists(channel_id)) == False:
        raise InputError('Invalid channel')

    for channel in channels:
        if (channel['channel_id'] == channel_id):
            channel['members'].append(create_member(u_id))   
        
    return {}

def channel_addowner(token, channel_id, u_id):
    

    print('u_id:' , u_id)

    if(channel_exists(channel_id) == False):
        raise InputError('Invalid channel_id') 
    elif (user_in_channel(get_u_id(token),channel_id) == False):
        raise AccessError('User not associated with channel')   
    elif((user_is_owner(u_id, channel_id) == True) or user_is_creator(u_id,channel_id) == True):
        raise InputError('User is already owner')  

    elif(user_in_channel(get_u_id(token),channel_id) != None):
        for channel in channels:
            if channel['channel_id'] == channel_id:
                channel['owners'].append(u_id)
    return {
    }

def channel_removeowner(token, channel_id, u_id):
    return {
    }
