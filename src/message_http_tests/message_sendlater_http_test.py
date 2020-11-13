'''
Http test for message_sendlater
'''
import requests
from datetime import datetime
SECRET = 'orangeTeam5'
def test_message_send_http(url):
    '''
    Http test for message_sendlater. Mostly the same as message_send, but
    with an extra timestamp
    '''

    #creating user data
    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    #registering user
    user = requests.post(f"{url}/auth/register", json=data)
    user_dict = user.json()

    #creating channel_data
    channel_data = {
        'token': user_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    #Creating channel
    channel = requests.post(f"{url}channels/create", json=channel_data)
    channel_dict = channel.json()

    moment = datetime.now()
    stamp_now = datetime.timestamp(moment) + 10

    #creating message data
    message_data = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'message': 'heeeyyyyyyyyy',
        'time_sent': stamp_now
    }

    #Sending a message, with valid timestamp
    resp = requests.post(f"{url}/message/sendlater", json=message_data)
    resp_dict = resp.json()

    assert resp.status_code == 200
    assert 'message_id' in resp_dict
    
