'''
Auth Functions
'''
from datetime import datetime
import sys
sys.path.append("..")
import jwt
import hashlib
from global_data import users
from error import InputError
from helper_functions import check, get_u_id, getUserData, saveUserData
NAME_MAXLEN = 50
NAME_MINLEN = 1
SECRET = 'orangeTeam5'

global users

def auth_login(email, password):
    '''
    functions logs in user
    '''
    # Check is email is invalid
    if not check(email):
        raise InputError('Invalid Email')

    # Handle case where no users registered
    if len(users) == 0:
        raise InputError('Email does not belong to a user')

    user_found = False
    user_details = {}

    #creating timestamp for token
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    #  Check if entered email is registered as a user

    for user in users:
        if user['email'] == email:
            user_found = True
            user_details = user.copy()
            # Check if entered password matches registered user's password
            if hashlib.sha256(password.encode()).hexdigest() != user_details['password']:
                raise InputError('Entered Password is Incorrect')

            user['token'] = jwt.encode({'u_id': user['u_id'], 'time': timestamp}, SECRET, algorithm='HS256')

            break

    # Raise exception if email is not registered
    if not user_found:
        raise InputError('Email does not belong to a user')

    # Return u_id and token upon successful login
    return {'u_id' : user_details['u_id'], 'token' : user_details['token']}

def auth_logout(token):
    '''
    function logs out user given valid token
    '''
    token_found = False

    # Search for matching active token
    for user in users:
        if token == user['token']:
            # Flag that active token was found and invalidate it to log out user
            token_found = True
            user['token'] = -1
            break

    return {
        'is_success': token_found,
    }


def auth_register(email, password, name_first, name_last):
    '''
    Function registers users
    '''
    #Code below checks if any users in the users dictionary and checks if input email already exists
    if not check(email):
        raise InputError('Invalid Email')

    if len(users) != 0:
        for user in users:
            if user['email'] == email:
                print("error")
                raise InputError('Email already registered')

    #Code below checks the length of the input names against restrictions
    if len(name_first) > NAME_MAXLEN or len(name_first) < NAME_MINLEN:
        raise InputError('Invalid First Name')

    if len(name_last) > NAME_MAXLEN or len(name_last) < NAME_MINLEN:
        raise InputError('Invalid Last Name')

    #Code below checks if input email is a valid email using regex

    #Code below checks the length of the password
    if len(password) < 6:
        raise InputError('Invalid password')
    #Code below is for when all conditions are met

    encoded_token = jwt.encode({'u_id': len(users) +1}, SECRET, algorithm='HS256')
    if check(email) and len(password) >= 6:
        #Create a new dictionary with data about the user
        new_user = {
            'u_id': len(users)+1,
            'name_first': name_first,
            'name_last': name_last,
            'handle_str': name_first.lower() + name_last[0],
            'email': email,
            'password': hashlib.sha256(password.encode()).hexdigest(),
            'token': encoded_token.decode('utf-8')
        }

        if len(users) == 0:
            new_user['permission_id'] = 1
        else:
            new_user['permission_id'] = 2

        #A copy of the dictionary is needed otherwise it messes with the references
        new_user_copy = new_user.copy()

        #Append the copied dictionary onto our list of users
        users.append(new_user_copy)

        saveUserData(users)
        #Return the correct output
        return {
            'u_id': new_user_copy['u_id'],
            'token': new_user_copy['token'],
        }
    return None
