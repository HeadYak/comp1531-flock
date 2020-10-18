import pytest
from auth import auth_register
from user import user_profile_setname
from global_data import users
from error import InputError
from other import clear

def test_user_profile_setname():
    clear()
    
    # creating users 
    user1 = auth_register('email1@gmail.com', 'password1', 'user1', 'userlast1')
    user2 = auth_register('email2@gmail.com', 'password2', 'user2', 'userlast2')
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']
    
    with pytest.raises(InputError):
        # first name is not between 1 and 50 characters
        user_profile_setname(token1, 'user1'*100, 'userlast1')
        # last name is not between 1 and 50 characters 
        user_profile_setname(token1, 'user1', 'userlast1'*100)
   
    # updating the users' names
    user_profile_setname(token1, 'auser1', 'useralast1')
    user_profile_setname(token2, 'user2', 'auserlast2')
    
    for user in users:
        if user['u_id'] == u_id1:
            assert user['name_first'] == 'auser1'
        if user['u_id'] == u_id2:
            assert user['name_last'] == 'auserlast2'
    
    clear()
    
