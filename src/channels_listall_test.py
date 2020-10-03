from channels import channels_listall, channels_create
from channel import channel_leave, channel_join
from auth import auth_register
import pytest
from other import clear

def test_channels_listall():
    clear()
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']

    #testing function returns an empty list before any channels have been made
    assert channels_listall(token1) == []

    #Creating channels to test channels_list.

    #test if only one channel in the dictionary
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    assert channels_listall(token1) == [ {'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 
                                          'creator':{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                          'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                          'members':[{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []} ]


    
    ch_id2 =channels_create(token2, "yetAnotherChannel", True)['channel_id']
    ch_id3 =channels_create(token1, "SameName", True)['channel_id']
    ch_id4 =channels_create(token2, "SameName", False)['channel_id']

    #test if multiple channels in the dictionary
    assert channels_listall(token1) == [ {'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 
                                         'creator':{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                         'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                         'members':[{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},

                                         {'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': True, 
                                          'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                          'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                          'members': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 'messages': []},

                                         {'channel_id': ch_id3, 'name': "SameName", 'is_public': True, 
                                          'creator': {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                          'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                          'members': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},

                                         {'channel_id': ch_id4, 'name': "SameName", 'is_public': False, 
                                          'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                          'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                          'members':[{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 'messages': []} ]


                                    
    channel_join(token1, ch_id2)
    channel_leave(token2, ch_id4)

    #checking the lists of channels have been updated after members have joined and left
    assert channels_listall(token1) ==  [ {'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 
                                         'creator':{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                         'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                         'members':[{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'},], 'messages': []},

                                         {'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': True, 
                                          'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                          'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                          'members': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'},
                                                      {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},

                                         {'channel_id': ch_id3, 'name': "SameName", 'is_public': True, 
                                          'creator': {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                          'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                          'members': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},

                                         {'channel_id': ch_id4, 'name': "SameName", 'is_public': False, 
                                          'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                          'owners': [], 
                                          'members':[], 'messages': []} ]