import sys
sys.path.append("..")

import requests
import json
import jwt
from other import clear

SECRET = 'orangeTeam5'

def test_auth_logout_http(url):
    '''
    A simple test to check echo
    '''
    clear()
    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    resp = requests.post(f"{url}/auth/register", json=data)
    r = requests.post(f"{url}/auth/logout", json={'token': jwt.encode({'u_id': 1}, SECRET, algorithm='HS256') })
    payload = r.json()
    print("Payload:", payload)
    assert payload['is_success']

    r = requests.post(f"{url}/auth/logout", json={'token': jwt.encode({'u_id': -1}, SECRET, algorithm='HS256') })
    payload = r.json()
    assert not payload['is_success']
