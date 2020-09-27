from auth import auth_register
from channels import channels_create
from global_data import channels

import pytest
from error import InputError


register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')

#Storing u_id generated from registration process in a variable for easy access
owner_u_id = register['u_id']

#Storing token generated from registration process in a variable for easy access
owner_token = register['token']


#Creating a channel thats public
def test_channels_create_ChannelPublic():
    new_channel = channels_create(register['token'] , "NameOfChannel" , True) 
    assert new_channel['channel_id'] == len(channels)

    #Check for if the channel_id of the new channel exists
    for channel in channels:
        if channel["channel_id"] == new_channel['channel_id']:
            pass


#Creating a channel thats not public
def test_channels_create_ChannelNotPublic():
    new_channel = channels_create(register['token'] , "NameOfChannel1" , False) 
    assert new_channel['channel_id'] == len(channels)

    #Check for if the channel_id of the new channel exists
    for channel in channels:
        if channel["channel_id"] == new_channel['channel_id']:
            pass

#Creating a channel with an invalid name
def test_channels_create_InvalidName():
    with pytest.raises(InputError):
        channels_create(register['token'] , "NameOfChannel"*100 , True)      

#Test for checking that whoever created the channel is an owner
def test_channels_create_OwnerCheck():
    new_channel = channels_create(register['token'] , "NameOfChannel" , True)
    channel_id = new_channel["channel_id"] 
    for channel in channels:
        if(channel["channel_id"] == channel_id):
            assert owner_u_id in channel["owners"]
            


    
