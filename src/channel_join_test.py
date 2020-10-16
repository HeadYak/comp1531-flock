'''
Nesacary imports
'''
import pytest
from channel import channel_join
from channels import channels_create
from auth import auth_register
from error import InputError, AccessError
from helper_functions import user_in_channel
from other import clear
from global_data import channels


def test_channels_join():
    '''
    tests for channel join
    '''
    clear()
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    user3 = auth_register("user3@gmail.com", "user3pass", "user3", "last3")
    token1 = user1['token']
    token2 = user2['token']
    token3 = user3['token']
    u_id2 = user2['u_id']
    u_id3 = user3['u_id']


    #creating channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "yetAnotherChannel", False)['channel_id']


    with pytest.raises(InputError):
        #test for invalid channel
        channel_join(token1, 50)

    with pytest.raises(AccessError):
        #test for user attempting to join private channel
        channel_join(token1, ch_id2)

    #checking after user has joined channels they are in the channels dictionary
    channel_join(token2, ch_id1)
    assert user_in_channel(u_id2, ch_id1)

    #testing muliplte people joining channel
    channel_join(token3, ch_id1)
    assert user_in_channel(u_id3, ch_id1)

    channel_join(token3, ch_id1)
    for channel in channels:
        if channel['channel_id'] == ch_id1:
            assert len(channel['members']) == 3
            break
