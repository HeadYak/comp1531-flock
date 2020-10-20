'''
A http test for channels_list
'''
import json
import requests

def test_channels_list_http(url):
    '''
    A http test for channels_list
    '''
    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    regis = requests.post(url + 'auth/register', data=registerdata)
    regis_dict = json.loads(regis.text)
    print('\n', regis_dict)
    data1 = {
        'token': regis_dict['token']
    }

    resp = requests.get(url + 'channels/list', params=data1)
    print(resp)
    resp_dict = json.loads(resp.text)
    assert resp_dict == []
    assert resp.status_code == 200

    channelcreatedata = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }
    resp = requests.post(url + 'channels/create', data=channelcreatedata)
    resp_dict = json.loads(resp.text)
    assert 'channel_id' in resp_dict
    assert resp.status_code == 200
