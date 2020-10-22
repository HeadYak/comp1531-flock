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

    regis = requests.post(f"{url}/auth/register", json=registerdata)
    regis_dict = regis.json()
    print('\n', regis_dict)
    token = {
        'token': regis_dict['token']
    }

    resp = requests.get(f"{url}/channels/list", json=token)
    print(resp)
    resp_dict = resp.json()
    assert resp_dict == {'channels' :[]}
    assert resp.status_code == 200

    channelcreatedata = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    newchan = requests.post(f"{url}/channels/create", json=channelcreatedata)
    newchan_dict = newchan.json()
    print("Newchan_dict:", newchan_dict)

    resp1 = requests.get(f"{url}/channels/list", json=token)
    resp1_dict = resp1.json()
    print("Resp1_dict:", resp1_dict)
    #Bugged need fix
    # assert resp_dict == [{'channel_id': 1 , 'name': 'Test_channel'}]
    assert resp1_dict == {'channels': [{'channel_id': 1, 'name': 'Test_channel'}]}
    