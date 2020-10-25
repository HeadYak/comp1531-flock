'''
Importing necessary functions to send requests to register and change permission
'''
import json
import sys
import requests

from helper_functions import resetData
from other import clear
sys.path.append('../')

def test_admin_userpermssion_change_http(url):
    '''
    Send request to register two users, before requesting a permission change.
    Asserting returned status code is 200
    '''
    resetData()
    clear()

    user_1_register = {
        'email' : 'first@gmail.com',
        'password' : 'Meep123',
        'name_first' : 'Sans',
        'name_last' : 'Undertale'
    }
    user_1 = requests.post(f"{url}/auth/register", json=user_1_register)
    user_1_details = user_1.json()
    user_1_token = user_1_details['token']

    user_2_register = {
        'email' : 'second@gmail.com',
        'password' : 'Meep123',
        'name_first' : 'Papyrus',
        'name_last' : 'Dundertale'
    }
    user_2 = requests.post(f"{url}/auth/register", json=user_2_register)
    user_2_details = user_2.json()
    user_2_id = user_2_details['u_id']

    permission_change_data = {
        'token' : user_1_token,
        'u_id' : user_2_id,
        'permission_id' : 1
    }

    resp = requests.post(f"{url}/admin/userpermission/change", json=permission_change_data)
    assert resp.status_code == 200
