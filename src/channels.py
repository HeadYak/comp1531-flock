'''
Funcstion for channels list, listall and messages
'''
from global_data import channels, users
from error import InputError
from helper_functions import create_member, user_in_channel, get_u_id, user_exists


def channels_list(token):
    '''
    Lists all current channels user is apart of
    '''
    u_id = get_u_id(token)
    user_channels = []
    for channel in channels:
        if user_in_channel(u_id, channel['channel_id']):
            user_channels.append(channel)
    return user_channels

def channels_listall(token):
    '''
    Lists all currents channels in flock
    '''
    if user_exists(get_u_id(token)):
        return channels
    return None

def channels_create(token, name, is_public):
    '''
    Creates a new channel
    '''
    valid_token = False
    for user in users:
        if user['token'] == token:
            valid_token = True

    if valid_token and len(name) <= 20:

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

    if len(name) > 20:
        raise InputError('Invalid Name')

    # print('Input token:' , token)
    # for user in users:
    #     print (user['token'])
    return None

