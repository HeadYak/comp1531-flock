import json
import requests

def test_standup_start_http(url):
    '''
    A http test for channels_create
    '''

    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    regis = requests.post(f"{url}/auth/register", json=registerdata)
    # regis_dict = json.loads(regis.text)
    regis_dict = regis.json()

    data1 = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    #Channels create always returning none
    resp = requests.post(f"{url}channels/create", json=data1)
    print('resp:', resp)
    resp_dict = resp.json()

    assert 'channel_id' in resp_dict
    assert resp.status_code == 200

    channel_id = resp_dict['channel_id']

    standup_data ={
        'token': regis_dict['token'],
        'channel_id': channel_id,
        'length': 3
    }


    resp = requests.post(f"{url}standup/start", json=standup_data)
    print('resp:', resp)
    resp_dict = resp.json()
    print('resp_dict:', resp_dict)
    assert resp.status_code == 200