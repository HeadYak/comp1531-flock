'''
Nessacary imports
'''
import jwt
import re 
from global_data import users, channels

SECRET = 'orangeTeam5'

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def user_in_channel(u_id, channel_id):
    '''
    checks if user is in channel
    '''
    found = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for member in channel['members']:
                if member['u_id'] == u_id:
                    found = True
    return found

def user_is_owner(u_id, channel_id):
    '''
    checks is user is owner
    '''
    found = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for owner in channel['owners']:
                if owner['u_id'] == u_id:
                    found = True
    return found

def user_is_creator(u_id, channel_id):
    '''
    checks is user is creator of channel
    '''
    result = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            if channel['creator']['u_id'] == u_id:
                result = True
    return result

def channel_exists(channel_id):
    '''
    checks if channel exists
    '''
    chan_exists = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            print("here")
            chan_exists = True
            return chan_exists
    return chan_exists

def user_exists(u_id):
    '''
    checks if user exists
    '''
    user = False
    for user in users:
        if user['u_id'] == u_id:
            user = True
    return user_exists

def get_u_id(token):
    '''
    gets user id given their token
    '''
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    return decoded['u_id']

def get_token(u_id):
    '''
    Gets token given u_id
    '''
    for user in users:
        if user['u_id'] == u_id:
            return user['token']

    return None

def create_member(u_id):
    '''
    creates a member dictionary for user
    '''
    for user in users:
        if user['u_id'] == u_id:
            name_first = user['name_first']
            name_last = user['name_last']
    return {
        'u_id': u_id,
        'name_first': name_first,
        'name_last': name_last,
    }

def user_a_member(u_id, channel_id):
    '''
    check if user is a member of a channel
    '''
    found = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for owners in channel['owners']:
                if owners['u_id'] == u_id:
                    found = True
    return found

def message_exists(message_id):
    '''
    checks if message exists
    '''
    found = False
    for channel in channels:
        for chan_messages in channel['messages']:
            if chan_messages['message_id'] == message_id:
                found = True
                return found
    return found

def message_creator(u_id, message_id):
    '''
    checks is user is creator of the message
    '''
    found = False
    for channel in channels:
        for chan_messages in channel['messages']:
            if chan_messages['creator'] == u_id and chan_messages['message_id'] == message_id:
                found = True
                return found
    return found

def find_channel(message_id):
    '''
    find the channel a message belongs to
    '''
    for channel in channels:
        for msg in channel['messages']:
            if msg['message_id'] == message_id:
                return channel['channel_id']
    return None

def check(email):
    '''
    Check if email is valid
    '''
    if re.search(regex,email):
        return True
    else:
        return False