'''
Http test for message_unreact
'''

import json
import requests
SECRET = 'orangeTeam5'
def test_message_send_http(url):
    '''
    Http test for auth_register
    '''

    #creating user data
    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    #registering a user
    user = requests.post(f"{url}/auth/register", json=data)
    user_dict = user.json()

    #creating channel data
    channel_data = {
        'token': user_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    #Creating channel
    channel = requests.post(f"{url}channels/create", json=channel_data)
    channel_dict = channel.json()

    #creating message data
    message_data = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'message': 'heeeyyyyyyyyy'
    }

    msg = requests.post(f"{url}/message/send", json=message_data)
    msg_dict = msg.json()

    # Creating react data
    react_data = {
        'token': user_dict['token'],
        'message_id': msg_dict['message_id'],
        'react_id' : 1
    }

    requests.post(f"{url}/message/react", json=react_data)

    # Creating unreact data
    unreact_data = {
        'token': user_dict['token'],
        'message_id': msg_dict['message_id'],
        'react_id' : 1
    }
    resp = requests.post(f"{url}/message/unreact", json=unreact_data)
    assert resp.status_code == 200

