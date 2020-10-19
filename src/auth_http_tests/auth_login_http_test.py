import sys
sys.path.append("..")

import requests
import json
from global_data import users

def test_auth_login_http(url):
    '''
    A simple test to check echo
    '''
    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    requests.post(url + 'auth/register', data=data)
    resp = requests.post(url + 'auth/login', data={'email': 'email@gmail.com', 'password' : 'HELLO123@'})
    assert resp.status_code == 200

