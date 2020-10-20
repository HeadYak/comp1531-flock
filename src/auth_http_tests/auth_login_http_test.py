'''
Http test for auth login
'''
import json
import requests

def test_auth_login_http(url):
    '''
    Http test for auth login
    '''
    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    logindata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@'
    }
    requests.post(url + 'auth/register', data=registerdata)
    resp = requests.post(url + 'auth/login', data=logindata)

    print("resp:", resp)
    resp_dict = json.loads(resp.text)
    assert 'u_id' in resp_dict
    assert 'token' in resp_dict
    assert resp.status_code == 200
