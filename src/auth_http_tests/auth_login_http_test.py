'''
Http test for auth login
'''
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
    requests.post(f"{url}/auth/register", json=registerdata)
    resp = requests.post(f"{url}/auth/login", json=logindata)

    print("resp:", resp)
    resp_dict = resp.json()
    assert 'u_id' in resp_dict
    assert 'token' in resp_dict
    assert resp.status_code == 200
