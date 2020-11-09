'''
HTTP tests for message pin
'''
import requests
SECRET = 'orangeTeam5'

def test_message_pin_http():
    '''
    HTTP test for auth register
    '''
    #creating data for user
    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    #registering user
    user = requests.post(f"{url}/auth/register", json=data)
    user_dict = user.json()

    #creating channel data
    channel_data = {
        'token': user_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    #Creating a channel
    channel = requests.post(f"{url}channels/create", json=channel_data)
    channel_dict = channel.json()

    #creating message data
    message_data = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'message': 'hello'
    }

    #sending a message
    message = requests.post(f"{url}/message/send", json=message_data)
    message_dict = message.json()

    #testing message pin
    resp = requests.post(f"{url}/message/pin", json=message_data)
    assert resp.status.code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

