import requests
import json

def test_auth_passwordreset_request_http(url):
  
    #creating user data
    registerdata = {
        'email': 'neve.parsons@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    #registering user
    resp = requests.post(f"{url}/auth/register", json=registerdata)
    assert resp.status_code == 200

    #testing auth passowrd reset 
    resp = requests.post(f"{url}/auth/passwordreset/request", json={'email': 'neve.parsons@gmail.com'})
    print(json.loads(resp.text))
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

    