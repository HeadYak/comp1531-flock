import sys
sys.path.append("..")


from channels import channels_list, channels_create
from channel import channel_join, channel_leave
from auth import auth_register
from other import clear


def test_channels_list():
    '''
    Tests for channels list
    '''
    clear()
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']

    #testing function returns an empty list before any channels have been made
    assert channels_list(token1) == []

    #Creating channels to test channels_list.

    #check for public channels
    channels_create(token1, "aGreatChannel", True)
    #check not public channels
    ch_id2 = channels_create(token2, "yetAnotherChannel", True)['channel_id']
    #check channels with same name
    channels_create(token1, "SameName", True)
    ch_id4 = channels_create(token2, "SameName", True)['channel_id']

    #Test for user2
    assert len(channels_list(token1)) == 2

    #Test for user1
    assert len(channels_list(token2)) == 2

    #check once user has joined channel it adds a member
    channel_join(token1, ch_id2)
    assert len(channels_list(token1)) == 3

    #check once user has left a channel they are no longer a member
    channel_leave(token2, ch_id4)
    assert len(channels_list(token2)) == 1
