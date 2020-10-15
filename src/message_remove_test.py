import pytest
from channel import channel_invite, channel_messages, channel_join
from message import message_send, message_remove
from channels import channels_create
from auth import auth_register
from error import InputError, AccessError
from other import clear
from global_data import channels
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
    ch_id2 = channels_create(token2, "yetAnotherChannel", True)['channel_id']

    #creating channel messages
    m_id1 = message_send(token1, ch_id1, 'hello')['message_id']
    m_id2 = message_send(token1, ch_id1, 'hey')['message_id']

    m_id3 = message_send(token2, ch_id2, "hello")['message_id']
    m_id4 = message_send(token2, ch_id2, "hello")['message_id']
    m_id5 = message_send(token2, ch_id2, "hello")['message_id']
         


    channel_join(token1, ch_id2)
    m_id6 = message_send(token1, ch_id2, "hello")['message_id']

    with pytest.raises(AccessError):
            #user id not created message and isnt an owner
            message_remove(token1, m_id3)

    #checking messages have been added
    assert len(channel_messages(token1, ch_id1, 0,)['messages']) == 2
    assert len(channel_messages(token2, ch_id2, 0,)['messages']) == 4

    
    #remove all messages
    message_remove(token1, m_id1)
    message_remove(token1, m_id2)

    #owner remove message they did not create
    message_remove(token2, m_id6)


    #checking messages have been removes
    assert len(channel_messages(token1, ch_id1, 0,)['messages']) == 0
    assert len(channel_messages(token2, ch_id2, 0,)['messages']) == 3

    for channel in channels:
        if channel['channel_id'] == ch_id2:
            print(channel['messages'])

    #error test
    with pytest.raises(InputError):
            #invalid message id
            message_remove(token1, m_id1)

   