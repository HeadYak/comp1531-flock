import sys
sys.path.append('../')

import json
import requests
from helper_functions import resetData, getChannelData, getUserData
def test_channel_invite_http(url):
    resetData()
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(url + 'auth/register', data=user1data)
    user1_dict = json.loads(user1.text)
    user1token = user1_dict['token']


    channel1 = {
        'token': user1token,
        'name': "Test_channel",
        'is_public': True
    }

    new_channel = requests.post(url + 'channels/create', data=channel1)
    assert new_channel.status_code == 200
    new_channel_dict = json.loads(new_channel.text)
    print("\nnew_channel_dict:" , new_channel_dict)
    channel_id = new_channel_dict['channel_id']

    channeldetailparam = {
        'token': user1token,
        'channel_id': channel_id
    }    

    channels = getChannelData()
    users = getUserData()

    print("\nChannels:\n", channels)
    print("\nUsers:\n", users)
    resp = requests.get(url + 'channel/details', params=channeldetailparam)
    print("\nresp:" , resp)
    resp_dict = json.loads(resp.text)
    print("\nresp_dict:" , resp_dict)
    #400 error code
    