import sys
sys.path.append("..")

#Assumption that whoever creates the channel is automatically an owner

from global_data import channels
from auth import auth_register
from channel import channel_addowner, channel_removeowner
from channels import channels_create
from error import InputError
from other import clear
import pytest

def test_channel_removeowner_owner():
    '''
    Tests removing an owner
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    #Storing token generated from registration process in a variable for easy access
    owner_token = register['token']
    #Registering another user
    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Jordan', 'Fitch', None)
    #Storing u_id generated from registration process in a variable for easy access
    nonowner_u_id = register1['u_id']
    #Using the registered user to create a channel
    new_channel = channels_create(owner_token, "Testing Channel", True)

    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']


    channel_addowner(owner_token, channel_id, nonowner_u_id)
    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert len(channel['owners']) == 2

    channel_removeowner(owner_token, channel_id, nonowner_u_id)

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert len(channel['owners']) == 1
    clear()

def test_channel_removeowner_already_not_owner():
    '''
    Test case for removing someone as owner when they are not owner
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)

    #Storing token generated from registration process in a variable for easy access
    owner_token = register['token']
    #Registering another user
    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Jordan', 'Fitch', None)
    #Storing u_id generated from registration process in a variable for easy access
    nonowner_u_id = register1['u_id']
    #Using the registered user to create a channel
    new_channel = channels_create(owner_token, "Testing Channel", True)

    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']
    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert nonowner_u_id not in channel['owners']
    with pytest.raises(InputError):
        channel_removeowner(owner_token, channel_id, nonowner_u_id)
    clear()

def test_channel_removeowner_invalidchannelid():
    '''
    Test case when attempting to remove someone as owner using an invalid channel_id
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)

    #Storing token generated from registration process in a variable for easy access
    owner_token = register['token']
    #Registering another user
    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Jordan', 'Fitch', None)
    #Storing u_id generated from registration process in a variable for easy access
    nonowner_u_id = register1['u_id']
    #Using the registered user to create a channel
    new_channel = channels_create(owner_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    with pytest.raises(InputError):
        channel_removeowner(owner_token, channel_id+100, nonowner_u_id)
    clear()
