from auth import auth_register, auth_passwordreset_request
from other import clear
from global_data import users

def test_auth_password_request_test():

    clear()
    #resgistering user to test
    auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    
    #checking a request assigns the user a reset code
    auth_passwordreset_request('validemail@gmail.com')

    for user in users:
        if user['u_id'] == 1:
            assert user['reset_code'] != 0
            break
