'''
Http test for messages
'''
import requests

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
    #registering user
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

    #sending message
    requests.post(f"{url}/message/send", json=message_data)

    #creating data for channel message end point
    chan_messages = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'start': 0
    }

    #Testing channel messages
    resp = requests.get(f"{url}/channel/messages", params=chan_messages)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert 'messages' and 'start' and 'end' in resp_dict