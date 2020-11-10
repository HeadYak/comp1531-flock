import sys
sys.path.append('../')
from auth import auth_register
from other import clear, users_all
from global_data import users, channels, messages

def test_users_all():
    '''
    Testing base case of showing registered user
    '''
    clear()
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    token1 = user1['token']

    print(users_all(token1))

    assert 'users' in users_all(token1)

def test_users_all_multiple():
    '''
    Testing if function returns multiple users
    '''
    clear()
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    token1 = user1['token']

    auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    auth_register("hello@gmail.com", "meep12", "name3", "last3")

    assert 'users' in users_all(token1)

