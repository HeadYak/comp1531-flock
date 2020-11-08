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
    user1 = auth_register("user1@gmail.com", "user1pass", "user1", "last1", None)
    user2 = auth_register("user2@gmail.com", "user2pass", "user2", "last2", None)
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

    #asserting search is finding correct number of messages
    assert len(search(token1, 'hey')['messages']) == 2
    assert len(search(token1, 'hey there')['messages']) == 1
    assert len(search(token1, 'he')['messages']) == 3
    assert len(search(token1, 'apple')['messages']) == 0

    assert len(search(token2, 'by')['messages']) == 2
    assert len(search(token2, 'byyyyeee')['messages']) == 1
    assert len(search(token2, 'hey')['messages']) == 1
    assert len(search(token2, 'apple')['messages']) == 0
