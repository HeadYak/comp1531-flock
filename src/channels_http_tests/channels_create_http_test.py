'''
A http test for channels_create
'''
import json
import requests


def test_channels_create_http(url):
    '''
    A http test for channels_create
    '''

    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    regis = requests.post(url + 'auth/register', json=registerdata)
    # regis_dict = json.loads(regis.text)
    regis_dict = regis.json()
    print('\nregis_dict:', regis_dict)
    data1 = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    #Channels create always returning none
    resp = requests.post(url + 'channels/create', json=data1)
    print('resp:', resp)
    resp_dict = json.loads(resp.text)
    print('resp_dict:', resp_dict)
    assert 'channel_id' in resp_dict
    assert resp.status_code == 200
