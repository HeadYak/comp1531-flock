from channel import channel_invite
from auth import auth_register
import pytest
import echo
from error import InputError
from global_data import users, channels
from helper_functions import user_in_channel


def channels_invite_test():
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", user1pass, user1, last1)
    user2 = auth_register("user2@gmail.com", user2pass, user2, last2)
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']
    
    #creating channels
    ch_id1 = channels_create(token1, aGreatChannel, True)
    ch_id2 =channels_create(token2, yetAnotherChannel, False)
    
    #not a valid channel
    with pytest.raises(InputError):
        #test for invalid channel
        channel_invite(token1, 50, u_id2)
        #test for invalid u_id
        channel_invite(token1, ch_id1, 3)
        #test for user not already member of the channel
        channel_invite(token2, ch_id1, u_id1)
    
    #test user invite works with public channel
    channel_invite(token1, ch_id1, u_id2)
    assert user_in_channel(u_id2, ch_id1) == True
    
    #test user invite works with private channel
    channel_invite(token2, ch_id2, u_id1)
    assert user_in_channel(u_id1, ch_id2) == True
    
    clear()
         
        
