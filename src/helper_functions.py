from global_data import users, channels
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



def channel_exists(channel_id):
    channel_exists = False
    for channel in channels:
        print(channel['channel_id'])
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

def get_token(u_id):
    for user in users:
        if (user['u_id'] == u_id):
            return user['token']    
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
   
def put_frank(u_id, channel_id):
    found = False
    for channel in channels:
        if(channel['creator']['u_id'] == u_id):
            found = True
            print(found)
        if (channel['channel_id'] == channel_id):
            for member in channel['members']:
                if (member['u_id'] == u_id):
                    found = True
                    print(found)
            if(channel['creator']['u_id'] == u_id):
                found = True
                print(found)
            for owner in channel['owners']:
                if (owner['u_id'] == u_id):
                    found = True
                    print(found)
