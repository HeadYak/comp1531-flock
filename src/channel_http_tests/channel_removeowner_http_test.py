'''
HTTP tests for channel_removeowner
'''
import json
import requests
import sys
sys.path.append('../')
from helper_functions import resetData, getChannelData, getUserData

def test_channel_removeowner_http(url):
    resetData()
    
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(url + 'auth/register', json=user1data)
    user1_dict = json.loads()
    user1token = user1_dict['token']
    
    # registers another user
    user2data = {
        'email': 'second@gmail.com',
        'password': 'HELLO123@!!!',
        'name_first': 'Howard',
        'name_last': 'Fog'
    }
    user2 = requests.post(f"{url}/auth/register", json=user2data)
    assert user2.status_code == 200

    #Extracts elements from the response dictionary and stores into variables
    user2_dict = user2.json()
    user2u_id = user2_dict['u_id']

    #creating channel
    channel1 = {
        'token': user1token,
        'name': "Test_channel",
        'is_public': True
    }

    new_channel = requests.post(url + 'channels/create', json=channel1)
    assert new_channel.status_code == 200
    new_channel_dict = json.loads(new_channel.text)

    channel_id = new_channel_dict['channel_id']

    #inviting user2 to channel
    channelinvitedata = {
        "token": user1token,
        "channel_id": channel_id,
        "u_id": user2u_id
    }  

    resp = requests.post(f"{url}/channel/invite", json=channelinvitedata)
    
    #adding user2 as an owner
    channel_add_owner = {
        'token': user1token,
        'channel_id': channel_id,
        'u_id': user2u_id
    }

    resp = requests.post(f"{url}/channel/addowner", json=channel_add_owner)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

    #testing remove_owner
    channel_remove_owner = {
        'token': user1token,
        'channel_id': channel_id,
        'u_id': user2u_id
    }

    resp = requests.post(f"{url}/channel/removeowner", json=channel_remove_owner)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

