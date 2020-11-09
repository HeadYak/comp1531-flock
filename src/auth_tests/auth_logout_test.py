'''
tests for auth logout
'''
import sys
sys.path.append("..")

from auth import auth_logout
from auth import auth_register
from other import clear
from error import AccessError
import pytest
# Testing giving a valid token
def test_auth_logout_valid():
    '''
    test valid login info
    '''
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    out_check = auth_logout(register['token'])
    assert out_check['is_success']

def test_auth_logout_invalid():
    '''
    test invalid login info
    '''
    with pytest.raises(AccessError):
        auth_logout(-1)
    
    clear()
    