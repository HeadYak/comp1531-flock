from channel import channel_invite, channel_messages
from message import message_send
from channels import channels_create
from auth import auth_register
import pytest
from error import InputError, AccessError
from global_data import messages
from helper_functions import user_in_channel
from other import clear

def test_channel_messages():
    #def test_channel_messages():
    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']


    #creating channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "yetAnotherChannel", False)['channel_id']

    with pytest.raises(InputError):
        channel_messages(token1, 50, 0)
        channel_messages(token1, ch_id1, 3)

    with pytest.raises(AccessError):
        channel_messages(token1, ch_id2, 0)



