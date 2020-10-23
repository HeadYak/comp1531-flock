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

    token = user_dict['token']

    user_data = {
        'token': token,
        'name_first': 'Neve',
        'name_last': 'Parsons'
    }

    #testing user profile setname
    resp = requests.put(f"{url}/user/profile/setname", json=user_data)
    assert resp.status_code == 200
    resp_dict = resp.json()
    assert resp_dict == {}

    '''
    user_data2 = {
        
        'token': token,
        'u_id': u_id
    }

    #checking names where changed
    #need to fix data storing for this to work 
    
    resp = requests.get(f"{url}/user/profile", params=user_data2)
    resp_dict = resp.json()
    assert resp_dict['name_first'] == 'Neve'
    assert resp_dict['name_last'] == 'Parsons'
    '''