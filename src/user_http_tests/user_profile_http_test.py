import requests

def test_user_profile_http(url):
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

    u_id = user_dict['u_id']
    token = user_dict['token']

    user_data = {
        'token': token,
        'u_id': u_id
    }

    #testing user profile
    resp = requests.get(f"{url}/user/profile", params=user_data)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {'u_id':1,
                         'email': 'email@gmail.com', 
                         'name_first': 'Frank', 
                         'name_last': 'Su', 
                         'handle_str': 'frankS'}