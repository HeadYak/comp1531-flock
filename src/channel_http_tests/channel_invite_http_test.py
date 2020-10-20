'''
A http test for channels_list
'''
import json
import requests

def test_channel_invite_http(url):
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(url + 'auth/register', data=user1data)
    user1_dict = json.loads(user1.text)
    user1token = user1_dict['token']

    user2data = {
        'email': 'second@gmail.com',
        'password': 'HELLO123@!!!',
        'name_first': 'Howard',
        'name_last': 'Fog'
    }
    user2 = requests.post(url + 'auth/register', data=user2data)
    assert user2.status_code == 200
    user2_dict = json.loads(user2.text)
    user2token = user2_dict['token']
    user2u_id = user2_dict['u_id']

    channel1 = {
        'token': user1token,
        'name': "Test_channel",
        'is_public': True
    }

    new_channel = requests.post(url + 'channels/create', data=channel1)
    assert new_channel.status_code == 200
    new_channel_dict = json.loads(new_channel.text)

    channel_id = new_channel_dict['channel_id']
    print("Token:" , user1token)
    print("Channel_id:" , channel_id)
    print("user_id:" , user2u_id)
    
    channelinvitedata = {
        'token': user1token,
        'channel_id': channel_id,
        'user_id': user2u_id
    }    
    resp = requests.post(url + 'channel/invite', data=channelinvitedata)
    print("Resp:" , resp)
    resp_dict = json.loads(resp.text)
    print("Resp_dict:" , resp_dict)

    token = {
        'token': user1token
    }
    temp = requests.post(f"{url}/channels/listall", params=token)
    temp_dict = json.loads(temp.text)
    # temp = requests.get(url + 'channels/listall', params=token)
    # temp_dict = json.loads(temp.text)
    print('temp_dict:', temp_dict)

    #Invalid channel error
    assert resp_dict == {}