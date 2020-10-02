from global_data import users, channels, messages
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
        raise AccessError('User not a member of channel')
    
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            channel['members'].append(create_member(u_id))   
    
    return {}

def channel_details(token, channel_id):
    u_id = get_u_id(token)
    if(channel_exists(channel_id) != True):
        raise InputError
    elif(user_in_channel(u_id, channel_id) != True):
        raise AccessError
    
    else:
        for channel in channels:
            if channel['channel_id'] == channel_id:

                return {
                    'name': channel['name'],
                    'owner_members': channel['owners'],
                    'all_members': channel['members']
                }

def channel_messages(token, channel_id, start):


    if (channel_exists(channel_id) == False):
        raise InputError('Invalid channel')
        
    if (user_in_channel(get_u_id(token), channel_id) == False):
        raise AccessError('User is not in channel')
    
    all_messages = []
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            all_messages = channel['messages']
            break
            
    all_messages = sorted(all_messages, key=lambda k: k['time_created'], reverse = True)
    
    total_messages = len(all_messages)
    
    if (start > (total_messages - 1)):
        raise InputError('Invalid start value')
    
    end = start + 50
    current_message = start
    
    channel_messages = []
    while current_message < end:
        if (current_message == total_messages):
            end = -1
            break
        channel_messages.append(all_messages[current_message])
        current_message += 1
        
    return {
        'messages': channel_messages,
        'start': start,
        'end': end,
    }


def channel_leave(token, channel_id):

    authorised_u_id = get_u_id(token)

    if (channel_exists(channel_id) == False):
        raise InputError('Invalid channel')
    
    if (user_in_channel(authorised_u_id, channel_id) == False):
        raise AccessError('User not a member of channel')

    for channel in channels:
        if (channel['channel_id'] == channel_id):
            for member in channel['members']:
                if (member['u_id'] == authorised_u_id):
                    channel['members'].remove(member)

                    
                    
    
    return {}

def channel_join(token, channel_id):
    
    u_id = get_u_id(token)
    

    if (channel_exists(channel_id)) == False:
        raise InputError('Invalid channel')

    public = False 
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            if (channel['is_public'] == True):
                public = True
    
    if (public == False):
        raise AccessError('Private Channel')
    
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
                channel['owners'].append(create_member(u_id))
                
    return {
    }

def channel_removeowner(token, channel_id, u_id):
    # for channel in channels:
    #     if channel['channel_id'] == channel_id:
    #         print('hello: ', channel['owners'])
    # print('input u_id: ' , u_id)
    if(channel_exists(channel_id) == False):
        raise InputError('Invalid channel_id')
    elif (user_in_channel(get_u_id(token),channel_id) == False):
        raise AccessError('User not associated with channel')   
    elif((user_is_owner(u_id, channel_id) == False) and user_is_creator(u_id,channel_id) == False):
        raise InputError('User is not owner')  
    elif(user_in_channel(get_u_id(token),channel_id) != None):
        for channel in channels:
            if channel['channel_id'] == channel_id:
                channel['owners'].remove(create_member(u_id))
    return {
    }
