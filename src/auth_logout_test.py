from auth import auth_logout
from auth import auth_register
import pytest
import echo
from error import InputError

# Testing giving a valid token
def test_auth_logout_valid():
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    outCheck = auth_logout(register['token'])
    assert outCheck['is_success'] == True

def test_auth_logout_invalid():
    badLog = auth_logout(-4)
    assert badLog['is_success'] == False
    
