from global_data import users, channels


def user_in_channel(u_id, channel_id):
    found = False
    for channel in channels:
        if (channel['channel_id'] == ch_id1):
            for member in channel['members']:
                if (member['u_id'] == u_id2):
                    found = True
    return found


def channel_exists(channel_id):
    channel_exists = False
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            channel_exists = True
            
    return channel_exists
            
def user_exists(u_id):            
    user_exists = False
    for user in users:
        if (user['u_id'] == u_id):
            user_exists = True
            
    return user_exists
    
def get_u_id(token):
    for user in users:
        if (user['token'] == token):
            return user['u_id']
    
def create_member(u_id):
    for user in users:
        if (user['u_id'] == u_id):
            name_fisrt = user['name_first']
            name_last = user['name_last']
    
    return {
        'u_id': u_id,
        'name_fisrt': name_fisrt,
        'name_last': name_last,
    }
   
