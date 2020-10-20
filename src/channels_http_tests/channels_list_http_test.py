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
    token = {
        'token': regis_dict['token']
    }

    resp = requests.get(url + 'channels/list', params=token)
    print(resp)
    resp_dict = json.loads(resp.text)
    assert resp_dict == {'channels' :[]}
    assert resp.status_code == 200

    channelcreatedata = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    newchan = requests.post(url + 'channels/create', data=channelcreatedata)
    newchan_dict = json.loads(newchan.text)
    print("Newchan_dict:", newchan_dict)

    resp1 = requests.get(url + 'channels/list', params=token)
    resp1_dict = json.loads(resp1.text)
    print("Resp1_dict:", resp1_dict)
    #Bugged need fix
    # assert resp_dict == [{'channel_id': 1 , 'name': 'Test_channel'}]
    assert resp1_dict == {'channels': [{'channel_id': 1, 'name': 'Test_channel'}]}
    