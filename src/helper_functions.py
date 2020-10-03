from global_data import users, channels

#checks if user is in channel
def user_in_channel(u_id, channel_id):
    found = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for member in channel['members']:
                if member['u_id'] == u_id:
                    found = True
    return found

def user_is_owner(u_id, channel_id):
    found = False
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            # print('hello: ' ,channel)
            for owner in channel['owners']:
                if (owner['u_id'] == u_id):
                    found = True
    return found


def user_is_creator(u_id, channel_id):
    result = False
    for channel in channels:
        if (channel['channel_id'] == channel_id):
            if channel['creator']['u_id'] == u_id:
                result = True
    return result


#checks if channel exists
def channel_exists(channel_id):
    channel_exists = False
    for channel in channels:
        print(channel['channel_id'])
        if (channel['channel_id'] == channel_id):
            channel_exists = True
            
    return channel_exists

#checks if user exists
def user_exists(u_id):            
    user_exists = False
    for user in users:
        if (user['u_id'] == u_id):
            user_exists = True
            
    return user_exists
    
#checks if get_u_id exists
def get_u_id(token):
    for user in users:
        if (user['token'] == token):
            return user['u_id']

#given a token finds users u_id
def get_token(u_id):
    for user in users:
        if (user['u_id'] == u_id):
            return user['token']    

#creates a member dictionary
def create_member(u_id):
    for user in users:
        if (user['u_id'] == u_id):
            name_first = user['name_first']
            name_last = user['name_last']
    
    return {
        'u_id': u_id,
        'name_first': name_first,
        'name_last': name_last,
    }
   
def user_a_member(u_id, channel_id):
    found = False
    for channel in channels:
        if channel['channel_id'] == channel_id:
            for owners in channel['owners']:
                if owners['u_id'] == u_id:
                    found = True
    return found