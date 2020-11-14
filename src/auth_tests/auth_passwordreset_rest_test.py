from auth import auth_register, auth_passwordreset_reset, auth_passwordreset_request
from other import clear
from global_data import users
from error import InputError
import pytest
import hashlib

def test_auth_password_reset_test():
    clear()

    #resgistering user to test
    auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    
    #requesting a password reset
    auth_passwordreset_request('validemail@gmail.com')

    for user in users:
        if user['u_id'] == 1:
            reset_code = user['reset_code']
            break


    with pytest.raises(InputError):
        #raise error if incorrect code
        auth_passwordreset_reset('12345', 'Agoodpassowrd')
        #raise error if bad bassword
        auth_passwordreset_reset(reset_code, 'bad')
        #raise error if both incorrect
        auth_passwordreset_reset('12345', 'bad')

    #test correct inputs change passowrd
    auth_passwordreset_reset(reset_code, 'Agoodpassowrd')
    for user in users:
        if user['u_id'] == 1:
            assert user['password'] ==  hashlib.sha256('Agoodpassowrd'.encode()).hexdigest()
            break

