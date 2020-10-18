import sys
sys.path.append("..")

from auth import auth_register 
from channels import channels_create
from channel import channel_addowner, channel_details

import pytest
from error import InputError, AccessError
from other import clear
def test_channel_details():
    clear()
    token = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')['token']
    channel_id = channels_create(token, 'TestChannel', True)['channel_id']
    
    assert len(channel_details(token, channel_id)) == 3 

#Testing for when a Channel ID is not a valid channel
def test_channel_details_InvalidChannel():
    clear()
    token = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')['token']
    channel_id = channels_create(token, 'TestChannel', True)['channel_id']
    with pytest.raises(InputError):
        channel_details(token, channel_id+100)
    
# Testing for when an authorised user is not a member of a channel
def test_channel_details_NotMember():
    clear()
    token = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')['token']
    channel_id = channels_create(token, 'TestChannel', True)['channel_id']
    token1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')['token']
    with pytest.raises(AccessError):
        channel_details(token1,channel_id)
        
