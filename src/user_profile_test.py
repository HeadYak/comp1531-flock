import pytest
from auth import auth_register
from user import user_profile
from error import InputError
from global_data import users
from other import clear

def test_user_profile():

    # creating users 
    user1 = auth_register('email1@gmail.com', 'password1', 'user1', 'userlast1')
    user2 = auth_register('email2@gmail.com', 'password2', 'user2', 'userlast2')
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']
    
    # User with u_id is not a valid user
    with pytest.raises(InputError):
        user_profile(3, 3)
        
    # creating user profiles
    user_profile(token1, u_id1)
    user_profile(token2, u_id2)
     
    assert user_profile(token1, u_id1) == {

    	'u_id': u_id1,
        'email': 'email1@gmail.com',
 	    'name_first': 'user1',
     	'name_last': 'userlast1',
        'handle_str': 'user1u',
        
    }
    assert user_profile(token2, u_id2) == {

    	'u_id': u_id2,
        'email': 'email2@gmail.com',
 	    'name_first': 'user2',
     	'name_last': 'userlast2',
        'handle_str': 'user2u',

    }


