import requests

def test_user_profile_setemail_http(url):
    #creating user
    user1 = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    user = requests.post(f"{url}/auth/register", json=user1)
    user_dict = user.json()
    assert user.status_code == 200

    token = user_dict['token']

    user_data = {
        'token': token,
        'email': 'updateemail@gmail.com'
    }
    
    #testing user profile setemail
    resp = requests.put(f"{url}/user/profile/setemail", json=user_data)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

