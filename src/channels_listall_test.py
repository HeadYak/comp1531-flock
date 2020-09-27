from channels import channels_listall
from auth import auth_register
import pytest

def channels_listall_test():
    #Creating users to create channels
    token1 = auth_register("user1@gmail.com", user1pass, user1, last1).token()
    token2 = auth_register("user2@gmail.com", user2pass, user2, last2).token()


    #Creating channels to test channels_list.

    #check for public channels
    ch_id1 = channels_create(token1, aGreatChannel, True)
    #check not public channels
    ch_id2 =channels_create(token2, yetAnotherChannel, False)
    #check channels with same name
    ch_id3 =channels_create(token1, SameName, True)
    ch_id4 =channels_create(token2, SameName, False)

    #should return list all the channels created
    assert channels_listall(token1) == [{'id': 1, 'name': "aGreatChannel", 'is_public': True},
                                        {'id': 2, 'name': "yetAnotherChannel", 'is_public': False},
                                        {'id': 3, 'name': "SameName", 'is_public': True},
                                        {'id': 4, 'name': "SameName", 'is_public': False}]
                                    
                                    

