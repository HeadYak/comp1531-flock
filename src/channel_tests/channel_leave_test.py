import sys
sys.path.append("..")

from channel import channel_invite, channel_leave
from channels import channels_create
from auth import auth_register
import pytest
from error import InputError, AccessError
from helper_functions import user_in_channel, user_a_member
from other import clear

def test_channels_leave():
    clear()

    #Creating users to create channels
    
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']
    
    #creating channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 =channels_create(token2, "yetAnotherChannel", False)['channel_id']
    
    with pytest.raises(InputError):
        #test for invalid channel
        channel_leave(token1, 50)

    with pytest.raises(AccessError):
        #test for user not already member of the channel
        channel_leave(token2, ch_id1)
        
    #test leaving a public channel    
    channel_leave(token1, ch_id1)
    assert user_in_channel(u_id1, ch_id1) == False
    
    #test leaving a private channel
    channel_leave(token2, ch_id2)
    assert user_in_channel(u_id2, ch_id2) == False
    assert user_a_member(u_id2, ch_id2) == False
    clear()

