import jwt
import pytest
from other import clear
from datetime import datetime
from error import AccessError
from auth import auth_register
from channels import channels_list, channels_create
from helper_functions import get_u_id
from global_data import users


SECRET = 'orangeTeam5'
FALSE_SECRET = 'orangeTeam27'

def test_check_token():
    clear()

    u_id = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)['u_id']

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    fake_token = jwt.encode({'u_id': 2, 'time': timestamp}, SECRET, algorithm='HS256')

    fake_token2 = jwt.encode({'u_id': u_id, 'time': timestamp}, FALSE_SECRET, algorithm='HS256')

    with pytest.raises(AccessError):
        channels_list(fake_token2)
        channels_create(fake_token, "name", True)
    
        

