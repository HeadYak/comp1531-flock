from global_data import users, channels
from helper_functions import get_u_id, create_member, resetData, \
    user_exists_persist, getUserData
from error import InputError, AccessError

def clear():
    resetData()
    del users[:]
    del channels[:]
    pass

def users_all(token):
    users = getUserData()
    u_id = get_u_id(token)

    if(user_exists_persist(int(u_id))):
        return {"users": users}
    else:
        return {}


def admin_userpermission_change(token, u_id, permission_id):
    owner_level = 1
    member_level = 2

    if permission_id not in (owner_level, member_level):
        raise InputError("Invalid permission id")

    for user in users:
        if user['token'] == token:
            if user['permission_id'] != owner_level:
                raise AccessError("You do not have permission for this command")
            break

    for user in users:
        if user['u_id'] == u_id:
            user['permission_id'] = permission_id
            return {}

    raise InputError("Specified user not found")


def search(token, query_str):
    '''
    Function finds matching strings to the one given and returns them, 
    only if the user is a member of the channel the message is in
    '''

    message_matches = []

    member = create_member(get_u_id(token))

    for channel in channels:
        if member in channel['members']:
            for msg in channel['messages']:
                if query_str in msg['message']:
                    message_matches.append(msg)

    return message_matches
