import sys
sys.path.append("..")

from auth import auth_register
from channels import channels_create
from global_data import channels
from error import InputError, AccessError
from other import clear
from standup import standup_start, standup_send
from helper_functions import getChannelData
import pytest


def test_standup_send_messagelen():
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            channel['is_standup'] == False

    standup_start(creator_token, channel_id, 3) 

    with pytest.raises(InputError):
        #message too long
        standup_send(creator_token, channel_id, 'h'*10001)

def test_standup_send_invalidchannel():
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            channel['is_standup'] == False

    standup_start(creator_token, channel_id, 3) 

    with pytest.raises(InputError):
        #invalid channel id
        standup_send(creator_token, channel_id*100 , 'h')


def test_standup_send_notinstandup():
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

     with pytest.raises(InputError):
        #Channel not in standup
        standup_send(creator_token, channel_id, 'h')


def test_standup_send_usernotinchannel():
    clear()
    channels = getChannelData()
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    

    #Registering a user
    register1 = auth_register('anothervalidemail@gmail.com', '!!!123abc!@#', 'Howard', 'Fog')
    #Storing token generated from registration process in a variable for easy access
    another_token = register1['token']



    #Using the registered user to create a channel
    new_channel = channels_create(creator_token, "Testing Channel", True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

     with pytest.raises(AccessError):
        #User not in channel
        standup_send(another_token, channel_id, 'h')