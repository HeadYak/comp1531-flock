'''
Nessacary imports
'''
import pytest
from channel import channel_join
from message import message_send, message_edit
from channels import channels_create
from auth import auth_register
from error import AccessError
from other import clear
from global_data import channels

def test_message_edit():
    '''
    Testing message_send function
    '''
    clear()

    #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2", None)
    token1 = user1['token']
    token2 = user2['token']

    #creating channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "yetAnotherChannel", True)['channel_id']

    #creating channel messages
    m_id1 = message_send(token1, ch_id1, 'hello')['message_id']
    message_send(token1, ch_id1, 'hey')
    m_id3 = message_send(token2, ch_id2, "hello")['message_id']
    message_send(token2, ch_id2, "hello")
    message_send(token2, ch_id2, "hello")

    channel_join(token1, ch_id2)
    m_id4 = message_send(token1, ch_id2, "hello")['message_id']

    with pytest.raises(AccessError):
        #user did not created message and isnt an owner
        message_edit(token2, m_id1, "message")

    #user editing thier own message
    message_edit(token1, m_id1, "newMessage")
    
    #owner of channel editing another users message/ empty string test
    message_edit(token2, m_id4, "")

    #owner of flcok editing a antoher users message
    message_edit(token1, m_id3, "yoooo")

    #checking old message is replaves by new message
    found = False
    for channel in channels:
        if channel['channel_id'] == ch_id1:
            for msg in channel['messages']:
                if msg['message_id'] == m_id1:
                    assert msg['message'] == "newMessage"
                if msg['message_id'] == m_id4:
                    assert msg['message'] == ""
                    found = True
                if msg['message_id'] == m_id3:
                    assert msg['message'] == "yoooo"

    #checking if string given is empty the message is removed
    assert found == False
