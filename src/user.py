import jwt
import requests
import os
from error import InputError
from global_data import users
from helper_functions import get_u_id, check, user_exists, change_picture, check_token
from PIL import Image
import urllib.request
from urllib.error import HTTPError

@check_token
def user_profile(token, u_id):
    '''
    For a valid user, return information on the user  
    '''
    new_u_id = get_u_id(token)
    '''
    Raise error if user with u_id is not a valid user 
    '''
    u_id = int(u_id)
    for user in users:
        if not user_exists(new_u_id) or new_u_id != u_id:
            raise InputError('Invalid User')
    
    for user in users:
        if user['u_id'] == u_id:
            return {
                'u_id': user['u_id'],
                'email': user['email'],
                'name_first': user['name_first'],
                'name_last': user['name_last'],
                'handle_str': user['handle_str'],
            }
@check_token
def user_profile_setname(token, name_first, name_last):
    u_id = get_u_id(token)
    '''
    Checks if the length of the user's name is within the set restrictions
    '''
    if (len(name_first) < 1 or len(name_first) > 50):
        raise InputError('Invalid First Name')
    
    if (len(name_last) < 1 or len(name_last) > 50):
        raise InputError('Invalid Last Name')

    for user in users:
        if user['u_id'] == u_id:
            user['name_first'] = name_first
            user['name_last'] = name_last
            break
    return {}

@check_token
def user_profile_setemail(token, email):
    u_id = get_u_id(token)
    '''
    Checking if the email entered is not a valid email 
    '''
    if check(email) == False:
        raise InputError('Invalid Email')
    '''
    Making sure that the email address is not already being used by another user
    '''
    for user in users:
        if user['email'] == email:
            raise InputError('Email is already being used')

    for user in users:
        if user['u_id'] == u_id:
            user['email'] = email
            break
    return {}

@check_token
def user_profile_sethandle(token, handle_str):
    '''
    Making sure handle_str is within character number limits, and is not taken
    by another user.
    '''
    if len(handle_str) < 3:
        raise InputError('Handle is too short')

    if len(handle_str) > 20:
        raise InputError('Handle is too long')

    for user in users:
        if user['handle_str'] == handle_str and user['token'] != token:
            raise InputError('This handle is already taken')

    for user in users:
        if user['token'] == token:
            user['handle_str'] = handle_str
            break
    return {}

@check_token
def user_profile_uploadphoto(token, img_url, x_start, y_start, x_end, y_end, url):

    u_id = get_u_id(token)

    profile_img_url = os.path.join("src/static/", str(u_id) + ".jpg")

    try:
        urllib.request.urlretrieve(img_url, profile_img_url)
    except HTTPError as e:
        raise InputError("Invalid url:", e)

    if (not img_url.endswith('jpg')):
        raise InputError("invalid file type")
    
    img = Image.open(profile_img_url)
    size = img.size

    if ( (x_start < 0) | (x_end > size[0]) | (y_start < 0) | (y_end > size[1]) ):
        raise InputError("Not valid start points")

    cropped = img.crop( (int(x_start), int(y_start), int(x_end), int(y_end)) )

    cropped.save(profile_img_url)

    profile_img_url = str(url) + profile_img_url

    change_picture(u_id, profile_img_url)

    return {}

