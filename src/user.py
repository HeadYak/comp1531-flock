from global_data import users
from error import InputError
from helper_functions import user_exists, get_u_id, check

def user_profile(token, u_id):
    # retrieve u_id from token
    u_id = get_u_id(token)
    # raise error if not a valid user
    if user_exists(u_id) == False:
        raise InputError('Invalid User')
    return {
        'u_id': user['u_id'],
        'email': user['email'],
        'name_first': user['name_first'],
        'name_last': user['name_last'],
        'handle_str': user['handle_str'],
    }

def user_profile_setname(token, name_first, name_last):
    u_id = get_u_id(token)
    # Checks if the length of the user's name is within the set restrictions
    if (len(name_first) < 1 or len(name_first) > 50):
        raise InputError('Invalid First Name')
    if (len(name_last) < 1 or len(name_last) > 50):
        raise InputError('Invalid Last Name')
    for user in users:
        if user['u_id'] == u_id:
            user['name_first'] == name_first
            user['name_last'] == name_last
            break

def user_profile_setemail(token, email):
    u_id = get_u_id(token)
    # Email entered is not a valid email
    if check(email) == False:
        raise InputError('Invalid Email')
    # Email address is already being used by another user
    for user in users:
        if user['email'] == email:
            raise InputError('Email is already being used')
    for user in users:
        if user['u_id'] == u_id:
            user['email'] == email
            break

def user_profile_sethandle(token, handle_str):
    return {
    }
