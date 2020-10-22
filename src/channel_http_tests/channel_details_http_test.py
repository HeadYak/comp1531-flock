'''
Http test for channel_details
'''
import json
import sys
import requests
sys.path.append('../')
from helper_functions import resetData, getChannelData, getUserData
def test_channel_details_http(url):
    '''
    Http test for channel_details
    '''
    resetData()
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(f"{url}/auth/register", json=user1data)
    user1_dict = user1.json()
    user1token = user1_dict['token']


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

    channeldetailparam = {
        'token': user1token,
        'channel_id': channel_id
    }

    channels = getChannelData()
    users = getUserData()

    print("\nChannels:\n", channels)
    print("\nUsers:\n", users)
    resp = requests.get(f"{url}channel/details", params=channeldetailparam)
    print("\nresp:" , resp)
    resp_dict = resp.json()
    print("\nresp_dict:" , resp_dict)
    assert 'name' in resp_dict
    assert 'owner_members' in resp_dict
    assert 'all_members' in resp_dict
    #400 error code
    