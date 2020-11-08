'''
File for server routes
'''

import sys
sys.path.append('../')

from json import dumps
from flask import Flask, request
from flask_cors import CORS
from error import InputError
from flask_mail import Mail, Message

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
from standup import *
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
mail= Mail(APP)

APP.config['MAIL_SERVER']='smtp.gmail.com'
APP.config['MAIL_PORT'] = 465
APP.config['MAIL_USERNAME'] = 'orangeteam5cs1531@gmail.com'
APP.config['MAIL_PASSWORD'] = 'OT5cs1531'
APP.config['MAIL_USE_TLS'] = False
APP.config['MAIL_USE_SSL'] = True
mail = Mail(APP)

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
    data = request.get_json()

    email = data['email']
    password = data['password']

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
    data = request.get_json()

    email = data['email']
    password = data['password']
    name_first = data['name_first']
    name_last = data['name_last']

    res = auth_register(email, password, name_first, name_last)
    
    return dumps(res)

@APP.route('/auth/passwordreset/request', methods=['POST']) 
def authpasswordresetrequest():
    data = request.get_json()
    email = data['email']
    code = auth_passwordreset_request(email)
    msg = Message("Password reset verification code", sender='orangeteam5cs1531@gmail.com',recipients=[email])
    msg.body = code
    mail.send(msg)
    return dumps ({})

@APP.route('/auth/passwordreset/reset', methods=['POST']) 
def authpasswordresetreset():
    data = request.get_json()
    res = auth_passwordreset_reset(data['reset_code'], data['new_password'])
    return dumps(res)

@APP.route('/channel/invite', methods=['POST'])
def channelinvite():
    data = request.get_json()

    token = data['token']
    channel_id = data['channel_id']
    u_id = data['u_id']
    
    res = channel_invite(token, channel_id, u_id)
    
    return dumps(res)

@APP.route('/channel/leave', methods=['POST'])
def channelleave():
    data = request.get_json()
    
    token = data['token']
    channel_id = data['channel_id']
    
    res = channel_leave(token, channel_id)
    
    return dumps(res)

@APP.route('/channel/details', methods=['GET'])
def channeldetails():
    '''
    Route for channel_invite
    '''
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    
    res = channel_details(token, channel_id)
    
    return dumps(res)

@APP.route('/channel/addowner', methods=['POST'])
def channeladdowner():
    '''
    Route for channel_addowner
    '''
    data = request.get_json()
    token = data['token']
    channel_id = data['channel_id']
    u_id = data['u_id']
    
    res = channel_addowner(token, channel_id, u_id)
    
    return dumps(res)

@APP.route('/channel/removeowner', methods=['POST'])
def channelremoveowner():
    '''
    Route for channel_removeowner 
    '''
    data = request.get_json()
    token = data['token']
    channel_id = data['channel_id']
    u_id = data['u_id']
    
    res = channel_removeowner(token, channel_id, u_id)
    
    return dumps(res)

@APP.route('/channel/join', methods=['POST'])
def channeljoin():
    '''
    Route for channel_join
    '''
    data = request.get_json()
    token = data['token']
    channel_id = data['channel_id']   
    
    res = channel_join_p(token, channel_id) 
    
    return dumps(res)

@APP.route('/channels/create', methods=['POST'])
def channelscreate():
    '''
    Route for channels_create
    '''
    data = request.get_json()

    token = data['token']
    name = data['name']
    is_public = data['is_public']
    
    res = channels_create(token, name, is_public)
    
    return dumps(res)

@APP.route('/channels/list', methods=['GET'])
def channelslist():
    '''
    Route for channels_list
    '''
    token = request.args.get('token')
    
    res = channels_list(token)
    
    return dumps(res)

@APP.route('/channels/listall', methods=['GET'])
def channelslistall():
    '''
    Route for channels_listall
    '''
    token = request.args.get('token')
    
    res = channels_list(token)
    
    return dumps(res) 

@APP.route('/channel/messages', methods=['GET'])
def channelmessages():
    '''
    Route for channel_messages
    '''
    token = request.args.get('token')
    channel_id = request.args.get('channel_id')
    start = request.args.get('start')
    
    res = channel_messages(token, channel_id, start)
    
    return dumps(res)

@APP.route('/message/send', methods=['POST'])
def messagesend():
    '''
    Route for message_send
    '''
    data = request.get_json()

    token = data['token']
    channel_id = data['channel_id']
    message = data['message']
    
    res = message_send(token, channel_id, message)
    
    return dumps(res)

@APP.route('/message/edit', methods=['PUT'])
def messageedit():
    '''
    Route for message_edit
    '''
    data = request.get_json()

    token = data['token']
    message_id = data['message_id']
    message = data['message']
    
    res = message_edit(token, message_id, message)
    
    return dumps(res)

@APP.route('/message/remove', methods=['DELETE'])
def messageremove():
    data = request.get_json()

    token = data['token']
    message_id = data['message_id']
    
    res = message_remove(token, message_id)
    
    return dumps(res)

@APP.route('/user/profile', methods=['GET'])
def userprofile():
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    
    res = user_profile(token, u_id)
    
    return dumps(res)

@APP.route('/user/profile/setname', methods=['PUT'])
def userprofilesetname():
    data = request.get_json()

    token = data['token']
    name_first = data['name_first']
    name_last = data['name_last']
    
    res = user_profile_setname(token, name_first, name_last)
    
    return dumps(res)

@APP.route('/user/profile/setemail', methods=['PUT'])
def userprofilesetemail():
    data = request.get_json()
    
    token = data['token']
    email = data['email']
    
    res = user_profile_setemail(token, email)
    
    return dumps(res)
    
@APP.route('/user/profile/sethandle', methods=['PUT'])
def userprofilesethandle():
    data = request.get_json()
    
    token = data['token']
    handle_str = data['handle_str']
    
    res = user_profile_sethandle(token, handle_str)

    return dumps(res)

@APP.route('/users/all', methods=['GET'])
def usersall():
    token = request.args.get('token')
    
    res = users_all(token)
    
    return dumps(res)

@APP.route('/search', methods=['GET'])
def search_http():
    token = request.args.get('token')
    query_str = request.args.get('query_str')
    
    resp = search(token, query_str)
    
    return dumps(resp)
    
@APP.route('/admin/userpermission/change', methods=['POST'])
def adminuserpermissionchange():
    '''
    Route for admin_userpermission_change
    '''
    data = request.get_json()

    token = data['token']
    user_id = data['u_id']
    permission = data['permission_id']

    res = admin_userpermission_change(token, user_id, permission)

    return dumps(res)

@APP.route('/clear', methods=['DELETE'])
def clear_http():
    '''
    Route for clear
    '''
    res = clear()
    return dumps(res)

@APP.route('/standup/start', methods=['POST'])    
def standupstart():
    data = request.get_json()

    token = data['token']
    channel_id = data['channel_id']
    length = data['length']
    
    res = standup_start(token, channel_id, length)

    return dumps(res)    

@APP.route('/standup/active', methods=['GET'])
def standupactive():
    data = request.get_json()
    token = data['token']
    channel_id = data['channel_id']

    res = standup_active(token, channel_id)

    return dumps(res)

@APP.route('/standup/send', methods=['POST'])
def standupsend():
    data = request.get_json()
    
    token = data['token']
    channel_id = data['channel_id']
    message = data['message']

    res = standup_send(token, channel_id, message)

    return dumps(res)

if __name__ == "__main__":
    APP.run(port=0, debug=True) # Do not edit this port
