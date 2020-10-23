import sys
sys.path.append('../')

import json
import requests
from helper_functions import resetData, getChannelData, getUserData
from other import clear


def test_channel_join_http(url):
    resetData()
    clear()
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(f"{url}/auth/register", json=user1data)
    user1_dict = user1.json()
    user1token = user1_dict['token']

    user2data = {
        'email': 'address@gmail.com',
        'password': 'PASSWORd',
        'name_first': 'Howard',
        'name_last': 'Fog'
    }
    user2 = requests.post(f"{url}/auth/register", json=user2data)
    user2_dict = user2.json()
    user2token = user2_dict['token']


    channel1 = {
        'token': user1token,
        'name': "Test_channel",
        'is_public': True
    }

    new_channel = requests.post(f"{url}/channels/create", json=channel1)
    assert new_channel.status_code == 200
    new_channel_dict = new_channel.json()
    print("\nnew_channel_dict:" , new_channel_dict)
    channel_id = new_channel_dict['channel_id']


    channeljoindata = {
        "token": user2token,
        "channel_id": channel_id
    }

    

    channels = getChannelData()
    print("Channels_before:\n", channels)

    resp = requests.post(f"{url}/channel/join", json=channeljoindata)

    channels = getChannelData()
    print("Channels_after:\n", channels)

    resp_dict = resp.json()
    print("Resp:\n", resp)
    print("Resp_dict:\n", resp_dict)

    