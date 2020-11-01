import requests
from helper_functions import getUserData, resetData

def test_auth_passwordreset_request_http(url):
  
    resetData()

    #creating user data
    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    #registering user
    requests.post(f"{url}/auth/register", json=registerdata)

    #requesting a password reset 
    resp = requests.post(f"{url}/auth/passwordreset/request", json={'email': 'email@gmail.com'})
    assert resp.status_code == 200

    #finding users status code 
    users = getUserData()
    for user in users:
        if user['u_id'] == 1:
            reset_code = user['reset code']
            break

    #testing password reset 
    resp = requests.post(f"{url}/auth/passwordreset/reset", json={'reset_code': reset_code,'new_password': "agoodpassword"})
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}