import sys
sys.path.append('../')
from auth import auth_register
from other import clear, users_all
from global_data import users, channels, messages

def test_users_all():
    clear()
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    token1 = user1['token']

    print(users_all(token1))

    assert 'users' in users_all(token1)