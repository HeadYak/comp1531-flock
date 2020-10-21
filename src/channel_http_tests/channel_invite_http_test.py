'''
A http test for channels_list
'''

import sys
sys.path.append('../')

import json
import requests
from global_data import channels
from helper_functions import getUserData, saveUserData , getChannelData ,saveChannelData, resetData
from other import clear

def test_channel_invite_http(url):
    resetData()
    clear()
    users = getUserData()
    channels = getChannelData()
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

    
    channelinvitedata = {
        'token': user1token,
        'channel_id': channel_id,
        'u_id': user2u_id
    }   

    channels = getChannelData()
    print("\nChannels:\n" , channels)
    users = getUserData()
    print("Users:\n" , users)

    resp = requests.post(f"{url}/channel/invite", data=channelinvitedata)
    print("Resp:", resp)
    resp_dict = resp.json()
    print("Resp_dict:", resp_dict)


    #400 error code invalid channel
    assert resp == {}