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
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2", None)
    token1 = user1['token']
    token2 = user2['token']

    #testing function returns an empty list before any channels have been made
    assert channels_list(token1) == {'channels':[]}

    #Creating channels to test channels_list.

    #check for public channels
    channels_create(token1, "aGreatChannel", True)
    #check not public channels
    ch_id2 = channels_create(token2, "yetAnotherChannel", True)['channel_id']
    #check channels with same name
    channels_create(token1, "SameName", True)

    #Test for user2
    assert len(channels_list(token1)['channels']) == 2

    #Test for user1
    assert len(channels_list(token2)['channels']) == 1

    #check once user has joined channel it adds a member
    channel_join(token1, ch_id2)
    assert len(channels_list(token1)['channels']) == 3


