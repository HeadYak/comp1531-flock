import sys
sys.path.append("..")

from channels import channels_listall, channels_create
from channel import channel_leave, channel_join
from auth import auth_register
from other import clear

def test_channels_listall():
    '''
    Tests for channel_listall
    '''
    clear()
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2", None)
    token1 = user1['token']
    token2 = user2['token']

    #testing function returns an empty list before any channels have been made
    assert channels_listall(token1) == {'channels':[]}

    #Creating channels to test channels_list.

    #test if only one channel in the dictionary
    channels_create(token1, "aGreatChannel", True)
    assert len(channels_listall(token1)['channels']) == 1

    #creating channels
    channels_create(token2, "yetAnotherChannel", True)['channel_id']
    channels_create(token1, "SameName", True)
    channels_create(token2, "SameName", False)['channel_id']

    #test if multiple channels in the dictionary
    assert len(channels_listall(token1)['channels']) == 4
