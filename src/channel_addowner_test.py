'''
Tests for channel_addowner
'''
import pytest
from global_data import channels
from auth import auth_register
from channel import channel_addowner
from channels import channels_create
from error import InputError, AccessError
from other import clear


def test_channel_addowner_owner():
    '''
    tests adding owner
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Howard', 'Everdun')
    nonowner_u_id = register1['u_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert len(channel['owners']) == 1

    channel_addowner(creator_token, channel_id, nonowner_u_id)
    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert len(channel['owners']) == 2
    clear()


def test_channel_addowner_alreadyowner():
    '''
    Test case for making someone an owner twice
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing u_id generated from registration process in a variable for easy access
    creator_u_id = register['u_id']
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert creator_u_id == channel['creator']['u_id']
    with pytest.raises(InputError):
        channel_addowner(creator_token, channel_id, creator_u_id)
    clear()




def test_channel_addowner_notowner():
    '''
    Test case for trying to make someone an owner while not being an owner
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Howard', 'Everdun')
    nonowner_u_id = register1['u_id']
    nonowner_token = register1['token']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert nonowner_u_id not in channel['owners']
    with pytest.raises(AccessError):
        channel_addowner(nonowner_token, channel_id, nonowner_u_id)

    clear()


def test_channel_addowner_invalidchannelid():
    '''
    Test case when attempting to make someone an owner using an invalid channel_id
    '''
    clear()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Howard', 'Everdun')
    nonowner_u_id = register1['u_id']
    with pytest.raises(InputError):
        channel_addowner(creator_token, channel_id*100, nonowner_u_id)

    clear()
    