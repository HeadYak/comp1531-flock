import sys
sys.path.append('../')

import json
import requests
from helper_functions import resetData, getUserData, getChannelData
from other import clear
from global_data import channels, messages

def test_search_http(url):
    '''
    Http test for search
    '''
    clear()
    channels = getChannelData()
    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user = requests.post(f"{url}/auth/register", json=data)
    user_dict = user.json()

    channel_data = {
        'token': user_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }
    #Channels create always returning none
    print("Channels:", channels)
    channel = requests.post(f"{url}channels/create", json=channel_data)
    channels = getChannelData()
    print("Channels:", channels)

    channel_dict = channel.json()


    message_data = {
        'token': user_dict['token'],
        'channel_id': channel_dict['channel_id'],
        'message': 'heeeyyyyyyyyy'
    }

    resp = requests.post(f"{url}/message/send", json=message_data)
    resp_dict = resp.json()
    assert resp.status_code == 200

    print(resp_dict)
    searchparam = {
        "token": user_dict['token'],
        "query_str": 'heeeyyyyyyyyy'
    }


    res = requests.get(f"{url}/search", params=searchparam)
    assert res.status_code == 200
    res_dict = res.json()
    print("Res:\n", res)
    print("Res_dict:\n", res_dict)