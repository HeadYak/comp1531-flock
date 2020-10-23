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
    channels = getChannelData()
    print("\nChannels_start:\n" , channels)
    users = getUserData()
    print("\nUsers_start:\n" , users)
    
    #Code block each registers a user
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(f"{url}/auth/register", json=user1data)
    user1_dict = user1.json()
    user1token = user1_dict['token']


    #Code block registers a user
    user2data = {
        'email': 'second@gmail.com',
        'password': 'HELLO123@!!!',
        'name_first': 'Howard',
        'name_last': 'Fog'
    }
    user2 = requests.post(f"{url}/auth/register", json=user2data)
    assert user2.status_code == 200

    #Extracts elements from the response dictionary and stores into varaibles

    user2_dict = user2.json()
    user2u_id = user2_dict['u_id']

    channel1 = {
        'token': user1token,
        'name': "Test_channel",
        'is_public': True
    }

    new_channel = requests.post(f"{url}/channels/create", json=channel1)
    assert new_channel.status_code == 200
    new_channel_dict = new_channel.json()

    channel_id = new_channel_dict['channel_id']

    print("\nUser1token:" , user1token)
    print("Channel_id:" , channel_id)
    print("User2id:" ,user2u_id)

    channelinvitedata = {
        "token": user1token,
        "channel_id": channel_id,
        "u_id": user2u_id
    }  

    

    resp = requests.post(f"{url}/channel/invite", json=channelinvitedata)
    print("\nResp:", resp)
    resp_dict = resp.json()
    print("Resp_dict:", resp_dict)

    channels = getChannelData()
    print("\nChannels_end:\n" , channels)
    users = getUserData()
    print("\nUsers_end:\n" , users)
    assert resp_dict == {}