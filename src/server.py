'''
File for server routes
'''

import sys
sys.path.append('../')

from json import dumps
from flask import Flask, request
from flask_cors import CORS
from error import InputError

# from auth import auth_login, auth_logout, auth_register
# from channel import channel_invite, channel_details, channel_messages,channel_leave,channel_join,channel_addowner,channel_removeowner
# from channels import channels_list, channels_listall, channels_create
# from message import message_send, message_remove, message_edit
from auth import *
from channel import *
from channels import *
from message import *
from global_data import *
from helper_functions import *
from other import *
from user import *

def defaultHandler(err):
    '''
    Error handler
    '''
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
CORS(APP)

APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)

# Example
@APP.route("/echo", methods=['GET'])
def echo():
    '''
    Route for echo
    '''
    data = request.args.get('data')
    if data == 'echo':
   	    raise InputError(description='Cannot echo "echo"')
    return dumps({
        'data': data
    })

@APP.route('/auth/login', methods=['POST'])
def authlogin():
    '''
    Route for auth_login
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    print('Email:'+email)
    print('Password:'+password)

    res = auth_login(email, password)
    
    return dumps(res)

@APP.route("/auth/logout", methods=['POST'])
def authlogout():
    token = request.get_json()

    r = auth_logout(token['token'])

    return dumps(r)


@APP.route('/auth/register', methods=['POST'])
def authregister():
    '''
    Route for auth_register
    '''
    email = request.form.get('email')
    password = request.form.get('password')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')

    print('Email:'+email)
    print('Password:'+password)
    print('name_first:'+name_first)
    print('name_last:'+name_last)

    res = auth_register(email, password, name_first, name_last)
    # res['token'] = res['token'].decode('utf-8')

    return dumps(res)



@APP.route('/channels/create', methods=['POST'])
def channelscreate():
    '''
    Route for channel_create
    '''
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')

    res = channels_create(token, name, is_public)
    print(res)
    return dumps(res)

@APP.route('/channels/list', methods=['GET'])
def channelslist():
    '''
    Route for channel_list
    '''
    token = request.args.get('token')
    res = channels_list(token)
    return dumps(res)


@APP.route('/channels/listall', methods=['GET'])
def channelslistall():
    '''
    Route for channel_listall
    '''
    token = request.args.get('token')
    res = channels_listall(token)
    return dumps(res)    
if __name__ == "__main__":
    APP.run(port=0, debug=True) # Do not edit this port
