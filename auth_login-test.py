from auth import auth_login
from auth import auth_register
import echo 
import pytest
from error import InputError
import re

# Regular expression for validating an email
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def test_auth_login_BaseCase():
    if (re.search(regex, email):
        result = auth_login('validemail@gmail.com', '123abc!@#')
        assert result == {
            'u_id': ' '
            'token': ' ',
        }

# Testing for attempt to login using an invalid email address 
def test_auth_login_InvalidEmail():
    with pytest.raises(InputError):
        auth_login('Notavalidemailaddress', '123abc!@#')
    
# Testing for attempt to login using an email address that does not belong to a user
def test_auth_login_NonExistingEmail():
    with pytest.raises(InputError):
        auth_login('Emaildoesnotbelongtoauser', '123abc!@#')

# Testing given an incorrect password 
def test_auth_login_IncorrectPassword():
    with pytest.raises(InputError):
        auth_login('validemail@gmail.com', 'abc')
    
