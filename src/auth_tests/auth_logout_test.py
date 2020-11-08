'''
tests for auth logout
'''
import sys
sys.path.append("..")

from auth import auth_logout
from auth import auth_register
from other import clear
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
    bad_log = auth_logout(-4)
    assert not bad_log['is_success']
    clear()
    