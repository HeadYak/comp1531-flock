import requests
from helper_functions import getUserData, resetData
import json

def test_auth_passwordreset_reset_http(url):
  
    resetData()

    #creating user data
    registerdata = {
        'email': 'neve.parsons@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    #registering user
    requests.post(f"{url}/auth/register", json=registerdata)

    #requesting a password reset 
    resp = requests.post(f"{url}/auth/passwordreset/request", json={'email': 'neve.parsons@gmail.com'})
    print(json.loads(resp.text))
    assert resp.status_code == 200

    #finding users status code 
    users = getUserData()
    for user in users:
        if user['u_id'] == 1:
            reset_code = user['reset_code']
            break

    print(users)

    #testing password reset 
    resp = requests.post(f"{url}/auth/passwordreset/reset", json={'reset_code': reset_code,'new_password': "agoodpassword"})
    print(json.loads(resp.text))
    assert resp.status_code == 200
    resp_dict = (json.loads(resp.text))
    assert resp_dict == {}