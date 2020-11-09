import pytest
from channel import channel_messages, channel_join
from message import message_send, message_remove
from channels import channels_create
from auth import auth_register
from error import InputError, AccessError
from other import clear

def test_message_pin():
    '''
    Testing message_pin function 
    '''
    clear()

    #creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']

    #creating channels
    ch_id1 = channels_create(token1, "FirstChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "SecondChannel", True)['channel_id']

    #creating channel messages
    m_id1 = message_send(token1, ch_id1, 'hello1')['message_id']
    m_id2 = message_send(token1, ch_id1, 'hello2')['message_id']
    m_id3 = message_send(token2, ch_id2, "hello3")['message_id']
    
    with pytest.raises(InputError):
        #invalid message_id 
        message_pin(token2, m_id4)
    
    #user pinning a message
    message_pin(token1, m_id1)
    
    with pytest.raises(InputError):
        #message is already pinned
        message_pin(token1, m_id1)
    
    with pytest.raises(AccessError):
        #unauthorised user that is not an owner or part of the channel 
        message_pin(token3, m_id1)
    
    message_pin(token1, m_id2)
    assert find_message(token1, ch_id1)
    
    clear()
    
