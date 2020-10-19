import sys
sys.path.append("..")

import requests
import json
from global_data import users
from other import clear
SECRET = 'orangeTeam5'
def test_auth_register_http(url):
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
    resp = requests.post(url + 'auth/register', data=data)
    assert resp.status_code == 200
    # assert json.loads(resp.text) == {'u_id': '', 'password' : 'HelloPassword!'}