'''
Required modules
'''
import pytest
from message import message_send, message_react
from channels import channels_create
from auth import auth_register
from error import InputError
from helper_functions import getChannelData
from other import clear

def test_messagereact_base():
    '''
    Testing if a react can be added to a message
    '''
    clear()

    # Registering user and creating a channel to send messages to
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    token1 = user1['token']
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']

    m_id = message_send(token1, ch_id1, 'hey')
    message_react(token1, m_id, 1)

    data = getChannelData()
    channel_list = data['channels']

    for channel in channel_list:
        for message in channel['messages']:
            assert len(message['reacts']) == 1
            for react in message['reacts']:
                if react['react_id'] == 1:
                    assert len(react['u_ids']) == 1
                    assert user1['u_id'] in react['u_ids']
                    break
            break
        break
        
    clear()

def test_messagereact_invalid_input():
    '''
    Testing if errors returned when given invalid input
    '''
    clear()

    # Registering users, creating channels and sending messages to both
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "ChannelTwo", True)['channel_id']

    m_id1 = message_send(token1, ch_id1, 'hey')
    m_id2 = message_send(token2, ch_id2, 'hello')

    # Trying to react to a non_existing message
    with pytest.raises(InputError):
        message_react(token1, m_id1 + 100, 1)

    # Trying to react with a non_existing react type
    with pytest.raises(InputError):
        message_react(token1, m_id1, 1000)

    # Trying to react to a message in a channel user has not joined
    with pytest.raises(InputError):
        message_react(token1, m_id2, 1)

    # Trying to react to the same message with the same react
    message_react(token1, m_id1, 1)
    with pytest.raises(InputError):
        message_react(token1, m_id1, 1)

    clear()
