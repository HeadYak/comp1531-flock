import sys
sys.path.append("..")

from auth import auth_register, users
import pytest
from auth import auth_register, users
from error import InputError
from other import clear
from helper_functions import getUserData
# from global_data import users


def test_auth_register_base_case():
    '''
    Test base case for auth_register
    '''
    clear()
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton', None)
    users = getUserData()
    assert len(users) == 1
    
    auth_register('andanothervalidemail@gmail.com', '123abc!@#*', 'Hayden', 'Everest', None)
    users = getUserData()
    assert len(users) == 2
    clear()

#Test case for attempting to register using an invalid email address
def test_auth_register_invalid_email():
    '''
    Tests invalid email
    '''
    with pytest.raises(InputError):
        auth_register('Thisisnotanemailaddress', '123abc!@#', 'Hayden', 'Everest', None)
    clear()

#Test case for when attempting to register with an email already used to register
def test_auth_register_existing_email():
    '''
    Tests existing email
    '''
    auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123abc!@#', 'Howard', 'Evererton', None)
        auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)

    clear()


#Test case when attempting to register with a password shorter than 6 characters
def test_auth_register_invalid_password():
    '''
    Test invalid password
    '''
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', 'Everest', None)

    clear()

#Test case for when attempting to register with a first name thats too long
def test_auth_register_invalid_first_name1():
    '''
    Tests invalid first name
    '''
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden'*100, 'Everest', None)

    clear()

#Test case for when attempting to register with a empty first name
def test_auth_register_invalid_first_name2():
    '''
    Tests invalid first name
    '''
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', '', 'Everest', None)

    clear()

#Test case for when attempting to register with a last name thats too long
def test_auth_register_invalid_last_name1():
    '''
    Tests invalid Last name
    '''
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', 'Everest'*100, None)

    clear()


#Test case for when attempting to register with a empty last name
def test_auth_register_invalid_last_name2():
    '''
    Tests invalid last name
    '''
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', '', None)

    clear()
