import sys
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
    data = request.args.get('data')
    if data == 'echo':
   	    raise InputError(description='Cannot echo "echo"')
    return dumps({
        'data': data
    })

@APP.route('/auth/login', methods=['POST'])
def authlogin():
    email = request.args.get('email')
    password = request.args.get('password')
    return dumps({
        'email': email,
        'password': password
    })

@APP.route('/auth/register', methods=['POST'])
def authregister():
    email = request.args.get('email')
    password = request.args.get('password')
    name_first = request.args.get('name_first')
    name_last = request.args.get('name_last')
    return dumps({
        'email': email,
        'password': password,
        'name_first': name_first,
        'name_last': name_last
    })

if __name__ == "__main__":
    APP.run(port=0 , debug=True) # Do not edit this port
