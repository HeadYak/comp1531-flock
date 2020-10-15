import pytest
from channel import channel_invite, channel_messages
from message import message_send
from channels import channels_create
from auth import auth_register
from error import InputError, AccessError
from other import clear

'''
Testing message_send function
'''


def test_message_send():
    
    clear()

    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']

    #creating channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "yetAnotherChannel", False)['channel_id']

    #error test
    with pytest.raises(InputError):
            #message too lond
            message_send(token1, ch_id1, 'h'*1001)

    with pytest.raises(AccessError):
            #user not in channel
            message_send(token1, ch_id2, "ilegal")


    #creating channel messages
    message_send(token1, ch_id1, 'h'*1000)
    message_send(token1, ch_id1, 'hey')

    message_send(token2, ch_id2, "hello")
    message_send(token2, ch_id2, "hello")
    message_send(token2, ch_id2, "hello")

    #checking messages have been added
    assert len(channel_messages(token1, ch_id1, 0,)['messages']) == 2
    assert len(channel_messages(token2, ch_id2, 0,)['messages']) == 3