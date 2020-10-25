'''
Http test for messages
'''
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

    #creating message data
    message_data = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'message': 'heeeyyyyyyyyy'
    }

    #Sedning  a message
    message = requests.post(f"{url}/message/send", json=message_data)
    message_dict = message.json()

    #creating data for message edit
    message_data2 = {
        'token': user_dict['token'],
        'message_id': message_dict['message_id'],
        'message': "heeeyyooooo"
    }

    #testing message edit
    resp = requests.put(f"{url}/message/edit", json=message_data2)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}