from auth import auth_login
from auth import auth_register
import echo 
import pytest
from error import InputError
from global_data import users
import re
from other import clear
# Regular expression for validating an email

def test_auth_login_BaseCase():
    clear()
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton')
    print(users)
    result = auth_login('anothervalidemail@gmail.com', '123abc!@#*')
    assert len(result) == 2

#Testing for attempt to login using an invalid email address 
    clear()
def test_auth_login_InvalidEmail():
    with pytest.raises(InputError):
        auth_login('Notavalidemailaddress', '123abc!@#')
    
# Testing for attempt to login using an email address that does not belong to a user
    clear()
def test_auth_login_NonExistingEmail():
    with pytest.raises(InputError):
        auth_login('Emaildoesnotbelongtoauser', '123abc!@#')

# Testing given an incorrect password 
    clear()
def test_auth_login_IncorrectPassword():
    with pytest.raises(InputError):
        auth_login('validemail@gmail.com', 'abc')
    
