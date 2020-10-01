from channels import channels_listall, channels_create
from channel import channel_leave, channel_join
from auth import auth_register
import pytest


def test_channels_listall():
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']

    assert channels_listall(token1) == []

    #Creating channels to test channels_list.

    #check for public channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)
    #check not public channels
    ch_id2 =channels_create(token2, "yetAnotherChannel", False)
    #check channels with same name
    ch_id3 =channels_create(token1, "SameName", True)
    ch_id4 =channels_create(token2, "SameName", False)

    #should return list all the channels created
    assert channels_listall(token1) ==  [{'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 'creator': token1, 'owners': [u_id1], 'members': [u_id1], 'messages': []}, 
                                         {'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': False, 'creator': token2, 'owners': [u_id2], 'members': [u_id2], 'messages': []},
                                         {'channel_id': ch_id3, 'name': "SameName", 'is_public': True, 'creator': token1, 'owners': [u_id1], 'members': [u_id1], 'messages': []},
                                         {'channel_id': ch_id4, 'name': "SameName", 'is_public': False, 'creator': token2, 'owners': [u_id2], 'members': [u_id2], 'messages': []}]
                                    
    channel_join(token1, ch_id2)
    channel_leave(token2, ch_id4)

    assert channels_listall(token1) ==  [{'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 'creator': token1, 'owners': [u_id1], 'members': [u_id1], 'messages': []}, 
                                         {'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': False, 'creator': token2, 'owners': [u_id2], 'members': [u_id2, u_id1], 'messages': []},
                                         {'channel_id': ch_id3, 'name': "SameName", 'is_public': True, 'creator': token1, 'owners': [u_id1], 'members': [u_id1], 'messages': []},
                                         {'channel_id': ch_id4, 'name': "SameName", 'is_public': False, 'creator': token2, 'owners': [], 'members': [], 'messages': []}]
