import pytest
from channel import channel_messages
from global_data import channels
from time import sleep
from datetime import datetime
from message import message_sendlater
from channels import channels_create
from auth import auth_register
from error import InputError, AccessError
from other import clear

def test_message_sendlater_base():
    '''
    Sees if valid message is sent after 10 seconds
    '''
    clear()

    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    token1 = user1['token']

    ch_id1 = channels_create(token1, "FirstChannel", True)['channel_id']

    moment = datetime.now()
    stamp_now = datetime.timestamp(moment) + 10

    message_sendlater(token1, ch_id1, "Hello World!", stamp_now)
    # Sleep to let the message be sent after a delay
    sleep(10.9)

    for channel in channels:
        if channel['channel_id'] == ch_id1:
            assert len(channel['messages']) == 1
            break

    clear()

def test_message_sendlater_invalid_input():
    '''
    Tests invalid messages, such as a message too long, invalid channel, and
    a time in the past
    '''
    clear()

    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    token1 = user1['token']

    ch_id1 = channels_create(token1, "FirstChannel", True)['channel_id']

    moment = datetime.now()
    stamp_now = datetime.timestamp(moment) + 10

    # Error raised with message too long
    with pytest.raises(InputError):
        message_sendlater(token1, ch_id1, "h"*1001, stamp_now)

    # Error raised with non-existing channel_id
    with pytest.raises(InputError):
        message_sendlater(token1, ch_id1 + 1, "meep", stamp_now)

    # Error raised with time in the past
    with pytest.raises(InputError):
        message_sendlater(token1, ch_id1, "meep", stamp_now - 40)

    clear()

def test_message_sendlater_invalid_user():
    '''
    Tests if error is raised when user who hasn't joined channel tries to
    post message
    '''
    clear()

    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2", None)
    token1 = user1['token']
    token2 = user2['token']

    ch_id1 = channels_create(token1, "TheChannel", False)['channel_id']

    moment = datetime.now()
    stamp_now = datetime.timestamp(moment) + 10

    with pytest.raises(AccessError):
        message_sendlater(token2, ch_id1, "Hello World!", stamp_now)

    clear()

