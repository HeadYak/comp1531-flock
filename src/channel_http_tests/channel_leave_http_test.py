import sys
sys.path.append('../')

import json
import requests
from helper_functions import resetData, getChannelData, getUserData

def test_channel_leave_http(url):
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(url + 'auth/register', json=user1data)
    user1_dict = json.loads(user1.text)
    user1token = user1_dict['token']


    channel1 = {
        'token': user1token,
        'name': "Test_channel",
        'is_public': True
    }

    new_channel = requests.post(url + 'channels/create', json=channel1)
    assert new_channel.status_code == 200
    new_channel_dict = json.loads(new_channel.text)


    channel_id = new_channel_dict['channel_id']

    channelleavedata = {
        "token": user1token,
        "channel_id": channel_id
    }

    channels = getChannelData()

    print("Before:\n" , channels)
    resp = requests.post(url + 'channel/leave', json=channelleavedata)

    
    channels = getChannelData()
    print("After:\n" , channels)
    resp_dict = json.loads(resp.text)
    print("\nResp:" , resp)
    print("\nResp_dict:" , resp_dict)