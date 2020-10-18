import pytest
from auth import auth_register
from user import user_profile_setemail
from global_data import users
from error import InputError
from other import clear

def test_user_profile_setemail():
    clear()
    
    # creating users 
    user1 = auth_register('email1@gmail.com', 'password1', 'user1', 'userlast1')
    user2 = auth_register('email2@gmail.com', 'password2', 'user2', 'userlast2')
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']
    
    with pytest.raises(InputError):
        # email entered is not a valid email
        user_profile_setemail(token, 'notavalidemailaddress')
        # email address is already being used by another user
        user_profile_setemail(token, 'email@gmail.com')
        user_profile_setemail(token3, 'email@gmail.com')
    
    # updating the users' email address
    user_profile_setemail(token1, 'updateemail1@gmail.com')
    user_profile_setemail(token2, 'updateemail2@gmail.com')
    
    for user in users:
        if user['u_id'] == u_id1:
            assert user['email'] == 'updateemail1@gmail.com'
        if user['u_id'] == u_id2:
            assert user['email'] == 'updateemail2@gmail.com'  
    
    clear()
         
    
