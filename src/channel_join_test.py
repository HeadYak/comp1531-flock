from channel import channel_invite
from auth import auth_register
import pytest
import echo
from error import InputError
from global_data import users, channels
from helper_functions import user_in_channel


def channels_leave_test():
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
        channel_join(token1, 50)
        #user attempting to join private channel
        channel_join(token1, ch_id2)
        
    channel_join(token2, ch_id1)
    assert user_in_channel(u_id2, ch_id1) == True

