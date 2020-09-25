
from channels import channels_list
from auth import auth_register
import pytest

def channels_list_test():
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

    assert channels_list(token1) == [{'id': 1, 'name': "aGreatChannel", 'public': True},
                                    {'id': 3, 'name': "SameName", 'public': True}]
                                    
                                    
    assert channels_list(token2) == [{'id': 2, 'name': "yetAnotherChannel", 'public': False},
                                    {'id': 4, 'name': "SameName", 'public': False}]                               
                                    

