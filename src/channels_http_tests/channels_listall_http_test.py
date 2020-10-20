'''
A http test for channels_listall
'''
import json
import requests

def test_channels_listall_http(url):
    '''
    A http test for channels_listall
    '''
    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    regis = requests.post(url + 'auth/register', data=registerdata)
    regis_dict = regis.json()
    print('\nregis_dict:', regis_dict)
    data1 = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }
    data2 = {
        'token': regis_dict['token'],
        'name': "Test_channel1",
        'is_public': True
    }
    token = {
        'token': regis_dict['token']
    }

    requests.post(url + 'channels/create', data=data1)

    requests.post(url + 'channels/create', data=data2)

    resp = requests.get(url + 'channels/listall', params=token)
    resp_dict = json.loads(resp.text)
    print('resp_dict:', resp_dict)
    assert resp_dict == {
        'channels': [{'channel_id': 1, 'name': 'Test_channel'},
                     {'channel_id': 2, 'name': 'Test_channel1'}]}
