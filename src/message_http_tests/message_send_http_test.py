'''
Http test for messages
'''

import json
import requests
SECRET = 'orangeTeam5'
def test_message_send_http(url):
    '''
    Http test for auth_register
    '''

    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user = requests.post(f"{url}/auth/register", json=data)
    user_dict = user.json()

    channel_data = {
        'token': user_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    #Channels create always returning none
    channel = requests.post(f"{url}channels/create", json=channel_data)
    channel_dict = channel.json()


    message_data = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'message': 'heeeyyyyyyyyy'
    }

    resp = requests.post(f"{url}/message/send", json=message_data)
    resp_dict = resp.json()
    assert resp.status_code == 200
   
    assert 'message_id' in resp_dict