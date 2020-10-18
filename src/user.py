from error import InputError
from global_data import users


def user_profile(token, u_id):
    return {
        'user': {
        	'u_id': 1,
        	'email': 'cs1531@cse.unsw.edu.au',
        	'name_first': 'Hayden',
        	'name_last': 'Jacobs',
        	'handle_str': 'hjacobs',
        },
    }

def user_profile_setname(token, name_first, name_last):
    return {
    }

def user_profile_setemail(token, email):
    return {
    }

def user_profile_sethandle(token, handle_str):
    if len(handle_str) < 3:
        raise InputError('Handle is too short')

    if len(handle_str) > 20:
        raise InputError('Handle is too long')

    for user in users:
        if user['handle_str'] == handle_str and user['token'] != token:
            raise InputError('This handle is already taken')

    for user in users:
        if user['token'] == token:
            print("success")
            user['handle_str'] = handle_str
            break
