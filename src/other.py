from global_data import users, channels
from error import InputError, AccessError

def clear():
    del users[:]
    del channels[:]
    pass

def users_all(token):
    return {
        users
    }

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
    return {
        'messages': [
            {
                'message_id': 1,
                'u_id': 1,
                'message': 'Hello world',
                'time_created': 1582426789,
            }
        ],
    }
