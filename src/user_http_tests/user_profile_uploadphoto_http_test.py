import json
import requests


def test_user_profile_uploadphoto_http(url):
    '''
    A http test for channels_create
    '''

    #resister user
    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    regis = requests.post(f"{url}/auth/register", json=registerdata)
    regis_dict = regis.json()

    #create channel so user is a member
    data1 = {
        'token': regis_dict['token'],
        'name': "Test_channel",
        'is_public': True
    }

    resp = requests.post(f"{url}/channels/create", json=data1)
    assert resp.status_code == 200

    img_data = {
        'token': regis_dict['token'],
        'img_url': "https://pyxis.nymag.com/v1/imgs/cbe/f4c/00a849914d501ee4b30ef830a8662bff2c-08-pepe-the-frog.rsquare.w700.jpg",
        'x_start': 0, 
        'y_start': 0,
        'x_end': 600, 
        'y_end': 600
    }

    resp = requests.post(f"{url}/user/profile/uploadphoto", json=img_data)
    print(resp.json())
    assert resp.status_code == 200
