'''
Nessacary imports
'''
from message import message_send
from channels import channels_create
from auth import auth_register
from other import clear, search

def test_search_test():
    '''
    Testing search function
    '''
    clear()
    print('hejhefjsdal;f')

     #Creating users to create channels
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1")
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2")
    token1 = user1['token']
    token2 = user2['token']

    #creating channels
    ch_id1 = channels_create(token1, "aGreatChannel", True)['channel_id']
    ch_id2 = channels_create(token2, "yetAnotherChannel", False)['channel_id']

    #creating channel messages
    message_send(token1, ch_id1, 'hey there')
    message_send(token1, ch_id1, 'hey')
    message_send(token1, ch_id1, 'hello')

    message_send(token2, ch_id2, "byyyyeee")
    message_send(token2, ch_id2, "bye")
    message_send(token2, ch_id2, "hey")

    assert len(search(token1, 'hey')) == 2
    assert len(search(token1, 'hey there')) == 1
    assert len(search(token1, 'he')) == 3
    assert len(search(token1, 'apple')) == 0

    assert len(search(token2, 'by')) == 2
    assert len(search(token2, 'byyyyeee')) == 1
    assert len(search(token2, 'hey')) == 1
    assert len(search(token2, 'apple')) == 0
