
from channels import channels_list, channels_create
from channel import channel_join, channel_leave
from auth import auth_register
import pytest
from other import clear


def test_channels_list():
    clear()
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']
    u_id1 = user1['u_id']
    u_id2 = user2['u_id']

    #testing function returns an empty list before any channels have been made
    assert channels_list(token1) == []

    #Creating channels to test channels_list.

    #check for public channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    #check not public channels
    ch_id2 =channels_create(token2, "yetAnotherChannel", True)['channel_id']
    #check channels with same name
    ch_id3 =channels_create(token1, "SameName", True)['channel_id']
    ch_id4 =channels_create(token2, "SameName", True)['channel_id']

    #Test for user2
    assert channels_list(token1) == [{'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 
                                      'creator':{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                      'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                      'members':[{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},

                                     {'channel_id': ch_id3, 'name': "SameName", 'is_public': True, 
                                      'creator': {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                      'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                      'members': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []}]

    #Test for user1                                                       
    assert channels_list(token2) == [{'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': True, 
                                      'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                      'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                      'members': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 'messages': []},

                                     {'channel_id': ch_id4, 'name': "SameName", 'is_public': True, 
                                      'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                      'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                      'members':[{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 'messages': []}]     


    #check once user has joined channel it adds a member                    
    channel_join(token1, ch_id2)
    assert channels_list(token1) ==  [{'channel_id': ch_id1, 'name': "aGreatChannel", 'is_public': True, 
                                      'creator': {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                      'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                      'members':[{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},

                                     {'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': True, 
                                      'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                      'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                      'members':[{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'},
                                                 {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'} ], 'messages': []},
                                                 
                                     {'channel_id': ch_id3, 'name': "SameName", 'is_public': True, 
                                      'creator':{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}, 
                                      'owners': [{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 
                                      'members':[{'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []},]
   
    #check once user has left a channel they are no longer a member                           
    channel_leave(token2, ch_id4)
    assert channels_list(token2) == [ {'channel_id': ch_id2, 'name': "yetAnotherChannel", 'is_public': True, 
                                      'creator': {'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}, 
                                      'owners': [{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'}], 
                                      'members':[{'u_id': u_id2, 'name_first': 'user2', 'name_last': 'last2'},
                                                 {'u_id': u_id1, 'name_first': 'user1', 'name_last': 'last1'}], 'messages': []}]
