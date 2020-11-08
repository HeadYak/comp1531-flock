import sys
sys.path.append("..")

from auth import auth_register
from channels import channels_create
from global_data import channels
from error import InputError, AccessError
from other import clear
from standup import standup_start, standup_active
from helper_functions import getChannelData
import pytest


def test_standup_active_invalidchannelid():
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert channel['is_standup'] == False

    with pytest.raises(InputError):
        standup_active(creator_token, channel_id*100)        


def test_standup_active_basecase():
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert channel['is_standup'] == False

    standup_start(creator_token, channel_id, 3)  

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert channel['is_standup'] == True         

    res = standup_active(creator_token, channel_id)      

    assert len(res) == 2  

def test_standup_active_usernotinchannel():   
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest', None)
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert channel['is_standup'] == False

    standup_start(creator_token, channel_id, 3)  

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert channel['is_standup'] == True         

    #Registering a user
    register1 = auth_register('anothervalidemail@gmail.com', '!!!123abc!@#', 'Howard', 'Fog',  None)
    #Storing token generated from registration process in a variable for easy access
    another_token = register1['token']

    with pytest.raises(AccessError):
        res = standup_active(another_token, channel_id)
    