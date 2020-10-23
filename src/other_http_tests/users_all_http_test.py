import sys
sys.path.append('../')

import json
import requests
from helper_functions import resetData, getUserData
from other import clear

def test_users_all_http(url):
    resetData()
    clear()
    user1data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user1 = requests.post(f"{url}/auth/register", json=user1data)
    user1_dict = user1.json()
    user1token = user1_dict['token']


    users = getUserData()

    print("Users:\n", users)
    usersallparam = {
        "token": user1token
    }


    resp1 = requests.get(f"{url}/users/all", params=usersallparam)
    resp1_dict = resp1.json()


    print("\nResp\n", resp1)
    print("Resp1_dict:", resp1_dict)

    assert 'users' in resp1_dict