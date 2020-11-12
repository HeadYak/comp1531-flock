'''
tests for auth login
'''
import sys
sys.path.append("..")


from auth import auth_login
from auth import auth_register
from error import InputError
from global_data import users
import pytest
from other import clear

# Regular expression for validating an email

def test_auth_login_base_case():
    '''
    Tests for auth login base case
    '''
    clear()
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton', None)
    print(users)
    result = auth_login('anothervalidemail@gmail.com', '123abc!@#*')
    assert len(result) == 2

#Testing for attempt to login using an invalid email address
    clear()
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton', None)
def test_auth_login_invalid_email():
    '''
    Test for invalid email
    '''
    with pytest.raises(InputError):
        auth_login('Notavalidemailaddress', '123abc!@#')
    clear()
# Testing for attempt to login using an email address that does not belong to a user

def test_auth_login_non_existing_email():
    '''
    test for non-existing email
    '''
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton', None)
    with pytest.raises(InputError):
        auth_login('Emaildoesnotbelongtoauser', '123abc!@#')

# Testing given an incorrect password
    clear()
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton', None)
def test_auth_login_incorrect_password():
    clear()
    '''
    test for incorrect password
    '''
    with pytest.raises(InputError):
        auth_login('anothervalidemail@gmail.com', 'abc')
    