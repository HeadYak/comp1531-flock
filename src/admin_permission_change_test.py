'''Importing libraries to register users, change and check permissions'''
import pytest
from other import admin_userpermission_change, clear
from auth import auth_register
from global_data import users
from error import InputError, AccessError

# Testing base case: User is an owner, and target is an existing user
def test_userpermssion_change_base():
    '''
    Register two users, with one being an owner, as the first to register.
    Owner will change the other user's permission from member to owner.
    '''
    clear()
    user_owner = auth_register('owner@gmail.com', '123abc!@#*', 'Bob', 'Ross')
    user_member = auth_register('member@gmail.com', '123abc!@#*', 'Jo', 'Ross')

    owner_token = user_owner['token']
    member_id = user_member['u_id']
    owner_level = 1

    admin_userpermission_change(owner_token, member_id, owner_level)

    for user in users:
        if user['u_id'] == member_id:
            assert user['permission_id'] == owner_level
            break

    clear()

# Testing if AccessError returned when member tries to change permissions
def test_userpermssion_change_member():
    '''
    Register two users, one owner as first to register, and the other member
    by default. Member will attempt to change owner's permission to member, only
    to get an AccessError.
    '''
    user_owner = auth_register('owner@gmail.com', '123abc!@#*', 'Bob', 'Ross')
    user_member = auth_register('member@gmail.com', '123abc!@#*', 'Jo', 'Ross')

    member_token = user_member['token']
    owner_id = user_owner['u_id']
    member_level = 2

    with pytest.raises(AccessError):
        admin_userpermission_change(member_token, owner_id, member_level)

    clear()

# Testing if InputError returned when permssion change for non-existing user
def test_userpermssion_change_notexist():
    '''
    Register one user, the owner as first to register. Attempts to change
    permission of a non-existing user, to get InputError returned.
    '''
    user_owner = auth_register('owner@gmail.com', '123abc!@#*', 'Bob', 'Ross')
    owner_token = user_owner['token']
    non_member_id = 99
    owner_level = 1

    with pytest.raises(InputError):
        admin_userpermission_change(owner_token, non_member_id, owner_level)

    clear()

# Testing is owner can change other owner's permssions
def test_userpermssion_change_other_owner():
    '''
    Register two users, with one being owner by default, and change the
    permission of the member to owner. Newly promoted owner should be able
    to change the permissions of the other owner.
    '''
    user_1 = auth_register('owner@gmail.com', '123abc!@#*', 'Bob', 'Ross')
    user_2 = auth_register('member@gmail.com', '123abc!@#*', 'Jo', 'Ross')

    token_1 = user_1['token']
    token_2 = user_2['token']

    id_1 = user_1['u_id']
    id_2 = user_2['u_id']

    owner_level = 1
    member_level = 2

    admin_userpermission_change(token_1, id_2, owner_level)
    admin_userpermission_change(token_2, id_1, member_level)

    for user in users:
        if user['u_id'] == id_1:
            assert user['permission_id'] == member_level
            break

    clear()
