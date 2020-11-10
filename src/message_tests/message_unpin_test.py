import pytest
from channel import channel_messages, channel_join
from message import message_send, message_remove, message_unpin, message_pin
from channels import channels_create
from auth import auth_register
from error import InputError, AccessError
from other import clear
from helper_functions import find_message
from datetime import datetime
import jwt

SECRET = 'orangeTeam5'

def test_message_unpin():
    '''
    Testing message_unpin function 
    '''
    clear()

    now = datetime.now()
    timestamp = datetime.timestamp(now)

    fake_token = jwt.encode({'u_id': 3, 'time': timestamp}, SECRET, algorithm='HS256')

    #creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']

    #creating channels
    ch_id1 = channels_create(token1, "FirstChannel", True)['channel_id']

    #creating channel messages
    m_id1 = message_send(token1, ch_id1, 'hello1')['message_id']
    m_id2 = message_send(token1, ch_id1, 'hello2')['message_id']
    
    with pytest.raises(InputError):
        #invalid message_id 
        message_unpin(token2, 4)
    
    #user pinning a message
    message_pin(token1, m_id1)
    
    #user unpinning a pinned message
    message_unpin(token1, m_id1)
    
    with pytest.raises(InputError):
        #message is already unpinned
        message_unpin(token1, m_id1)

    message_pin(token1, m_id1)
    with pytest.raises(AccessError):
        #unauthorised user that is not an owner or part of the channel 
        message_unpin(fake_token, m_id1)
    
    message_pin(token1, m_id2)
    message = find_message(ch_id1, m_id2)
    assert message['is_pinned']

    message_unpin(token1, m_id2)
    message = find_message(ch_id1, m_id2)
    assert not message['is_pinned']
    
    clear()
    
