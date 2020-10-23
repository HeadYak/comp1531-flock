'''Importing libraries to pytest, to register users, and to set their handles'''
import pytest
from user import user_profile_sethandle
from auth import auth_register
from other import clear
from global_data import users
from error import InputError

# Testing a basic valid handle, where no one else has registered yet
def test_sethandle_base_case():
    '''
    Registering user, and giving them a handle where its number of characters is
    between 3 and 20 inclusive.
    '''
    clear()
    holder = auth_register('atest@gmail.com', '123abc!@#*', 'Howard', 'Everton')
    user_token = holder['token']
    user_profile_sethandle(user_token, "Gr8Handlem8")

    the_user = users[0]
    assert the_user['handle_str'] == "Gr8Handlem8"
    clear()

# Testing if error is returned when given a handle that is too short
def test_sethandle_short_case():
    '''
    Registering user, and giving them a handle where its number of characters is
    below 3.
    '''
    holder = auth_register('atest@gmail.com', '123abc!@#*', 'Howard', 'Everton')
    user_token = holder['token']

    with pytest.raises(InputError):
        user_profile_sethandle(user_token, "Gr")

    clear()

# Testing if error is returned when given a handle that is too long
def test_sethandle_long_case():
    '''
    Registering user, and giving them a handle where its number of characters is
    above 20.
    '''
    holder = auth_register('atest@gmail.com', '123abc!@#*', 'Howard', 'Everton')
    user_token = holder['token']

    with pytest.raises(InputError):
        user_profile_sethandle(user_token, "thisisasuperlonghandl")

    clear()

# Testing if error is returned when given a handle that's already been taken
def test_sethandle_taken_case():
    '''
    Registering user, and giving them a handle that has been taken by another
    registered user.
    '''
    user_1 = auth_register('atest@gmail.com', '123abc!@#*', 'Howard', 'Everton')
    user1_token = user_1['token']

    user_2 = auth_register('hello@gmail.com', '123abc!@#*', 'Bob', 'Jones')
    user2_token = user_2['token']

    user_profile_sethandle(user1_token, "MyHandle")

    with pytest.raises(InputError):
        user_profile_sethandle(user2_token, "MyHandle")
