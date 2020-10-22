'''
Http test for auth_register
'''
import json
import requests
SECRET = 'orangeTeam5'
def test_auth_register_http(url):
    '''
    Http test for auth_register
    '''

    data = {
        'email': 'email@gmail.com',
        'password': 'HELLO123@',
        'name_first': 'Frank',
        'name_last': 'Su'
    }
    resp = requests.post(url + 'auth/register', json=data)
    resp_dict = json.loads(resp.text)
    assert 'u_id' in resp_dict
    assert 'token' in resp_dict
    assert resp.status_code == 200
