from auth import auth_register 
from channels import channels_create
from channel import channel_addowner 

import pytest
import echo 
from error import InputError, AccessError

def test_channel_details():
    token = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest').token()
    channel_id = channels_create(token, TestChannel, True) 
    
    assert channel_details({'name': 'TestChannel', 'owners', 'members'})

#Testing for when a Channel ID is not a valid channel
def test_channel_details_InvalidChannel():
    with pytest.raises(InputError):
        channel_details('Notavalidchannel', 'owners', 'members'})
    
#Testing for when an authorised user is not a member of a channel
def test_channel_details_NotMember():
    with pytest.raises(AccessError):
        channel_details('name': 'InaccessibleChannel', 'owners', 'members'})
        
