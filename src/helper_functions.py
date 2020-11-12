'''
Nessacary imports
'''
import jwt
import re 
from global_data import users, channels
import json
from error import InputError, AccessError

SECRET = 'orangeTeam5'

regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def user_in_channel(u_id, channel_id):# pragma: no cover
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
def user_in_channel_persist(u_id, channel_id):# pragma: no cover
    channels = getChannelData()
    '''
    checks if user is in channel
    '''
    found = False
    for channel in channels:
        if int(channel['channel_id']) == int(channel_id):
            for member in channel['members']:
                if int(member['u_id']) == int(u_id):
                    found = True
    return found    

def user_is_owner(u_id, channel_id):# pragma: no cover
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

def user_is_creator(u_id, channel_id):# pragma: no cover
    '''
    checks is user is creator of channel
    '''
    result = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            if channel['creator']['u_id'] == u_id:
                result = True
    return result

def channel_exists(channel_id):# pragma: no cover
    '''
    checks if channel exists
    '''
    chan_exists = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            chan_exists = True
            return chan_exists
    return chan_exists

def channel_exists_persist(channel_id):# pragma: no cover
    '''
    checks if channel exists
    '''
    channels = getChannelData()
    chan_exists = False
    for channel in channels:
        if int (channel['channel_id']) == int(channel_id):
            chan_exists = True
            # return chan_exists
    return chan_exists

def user_exists(u_id):# pragma: no cover
    '''
    checks if user exists
    '''
    found = False
    for user in users:
        if user['u_id'] == u_id:
            found = True
            return found
    return found

def user_exists_persist(u_id):# pragma: no cover
    '''
    checks if user exists
    '''
    users = getUserData()
    user = False
    for user in users:
        if user['u_id'] == u_id:
            user = True
    return user_exists

def get_u_id(token):# pragma: no cover
    '''
    gets user id given their token
    '''
    try:
        decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
        return decoded['u_id']
    except Exception:
        raise AccessError("Invalid token")
def get_token(u_id):# pragma: no cover
    '''
    Gets token given u_id
    '''
    for user in users:
        if user['u_id'] == u_id:
            return user['token']

    return None

def create_member(u_id):# pragma: no cover
    '''
    creates a member dictionary for user
    '''
    for user in users:
        if user['u_id'] == u_id:
            name_first = user['name_first']
            name_last = user['name_last']
            url = user['profile_img_url']
    return {
        'u_id': u_id,
        'name_first': name_first,
        'name_last': name_last,
        'profile_img_url': url,
    }

def user_a_member(u_id, channel_id):# pragma: no cover
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

def user_a_member_persist(u_id, channel_id):# pragma: no cover
    '''
    check if user is a member of a channel
    '''
    channels = getChannelData()
    found = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for owners in channel['owners']:
                if owners['u_id'] == u_id:
                    found = True
    return found    

def message_exists(message_id):# pragma: no cover
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

def message_creator(u_id, message_id):# pragma: no cover
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

def find_message(channel_id, message_id):# pragma: no cover
    '''
    find a message in a channel
    '''
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for message in channel['messages']:
                if message['message_id'] == message_id:
                    return message
    return None

def find_channel(message_id):# pragma: no cover
    '''
    find the channel a message belongs to
    '''
    for channel in channels:
        for msg in channel['messages']:
            if msg['message_id'] == message_id:
                return channel['channel_id']
    return None

def check(email):# pragma: no cover
    '''
    Check if email is valid
    '''
    if re.search(regex,email):
        return True
    else:
        return False

def permission(u_id):# pragma: no cover
     '''
     find users premission
     '''
     for user in users:
         if user['u_id'] == u_id:
             return user['permission_id']
     return None

def change_picture(u_id, image_url): # pragma: no cover
    for channel in channels:
        for member in channel['members']:
            if member['u_id'] == u_id:
                member['profile_img_url'] = image_url
        for owner in channel['owners']:
            if owner['u_id'] == u_id:
                owner['profile_img_url'] = image_url
        for user in users:
            if user['u_id'] == u_id: 
                user['profile_img_url'] = image_url

def check_token(function): # pragma: no cover
    def wrapper(*args, **kwargs):
        token = args[0]
        print(user_exists(get_u_id(token)))
        if token == -1:
            raise AccessError("User is logged off")

        print(user_exists(get_u_id(token)))

        if not user_exists(get_u_id(token)):
            raise AccessError("Token is not valid")

        return function(*args, **kwargs)
    return wrapper


def getUserData():# pragma: no cover
    with open('./src/persistent_data/user_data.json', 'r') as FILE:
        DATA_STRUCTURE = json.load(FILE)
        return DATA_STRUCTURE['users']

def getChannelData():# pragma: no cover
    with open('./src/persistent_data/channel_data.json', 'r') as FILE:
        DATA_STRUCTURE = json.load(FILE)
        return DATA_STRUCTURE['channels']     

def saveUserData(users):# pragma: no cover
    DATA_STRUCTURE = {'users': users}
    with open('./src/persistent_data/user_data.json', 'w') as FILE:
    #print(json.dumps(DATA_STRUCTURE))
        json.dump(DATA_STRUCTURE, FILE)
    return

def saveChannelData(channels):# pragma: no cover
    DATA_STRUCTURE = {'channels': channels}
    with open('./src/persistent_data/channel_data.json', 'w') as FILE:
        json.dump(DATA_STRUCTURE, FILE)
    return         

def resetData():# pragma: no cover
    saveUserData([])
    saveChannelData([])

    return
