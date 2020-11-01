import requests

def test_auth_passwordreset_request_http(url):
  
    #creating user data
    registerdata = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }

    #registering user
    requests.post(f"{url}/auth/register", json=registerdata)

    #testing auth passowrd reset 
    resp = requests.post(f"{url}/auth/passwordreset/request", json={'email': 'email@gmail.com'})
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

    