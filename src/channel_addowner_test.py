#Assumption that whoever creates the channel is automatically an owner

from global_data import channels
from auth import auth_register
from channel import channel_addowner
from channels import channels_create 
from helper_functions import get_u_id
import pytest
from error import InputError, AccessError
from other import clear


def test_channel_addowner_owner():
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing u_id generated from registration process in a variable for easy access
    creator_u_id = register['u_id']
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token , "Testing Channel" , True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    register1 = auth_register('anothervalidemail@gmail.com', '123abc!@#', 'Howard', 'Everdun')
    nonowner_u_id = register1['u_id']

    print(channels)
    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert len(channel['owners']) == 0

    channel_addowner(creator_token, channel_id, nonowner_u_id)
    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert len(channel['owners']) == 1
    clear()

#Test case for making someone an owner twice
def test_channel_addowner_alreadyowner():
    #Registering a user
    register = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    #Storing u_id generated from registration process in a variable for easy access
    creator_u_id = register['u_id']
    #Storing token generated from registration process in a variable for easy access
    creator_token = register['token']
    #Using the registered user to create a channel
    new_channel = channels_create(creator_token , "Testing Channel" , True)
    #Storing channel_id generated from channel creation in a variable for easy access
    channel_id = new_channel['channel_id']

    for channel in channels:
        if channel['channel_id'] == channel_id:
            assert creator_u_id == channel['creator']
    with pytest.raises(InputError):
        channel_addowner(creator_token, channel_id, creator_u_id)




# #Test case for trying to make someone an owner while not being an owner
# def test_channel_addowner_notowner():
#     for channel in channels:
#         if channel['channel_id'] == channel_id:
#             assert nonowner_u_id not in channel['owners']
#     with pytest.raises(AccessError):
#         channel_addowner(nonowner_token, channel_id, nonowner_u_id)


#Test case when attempting to make someone an owner using an invalid channel_id
# def test_channel_addowner_invalidchannelid():
#     with pytest.raises(InputError):
#         channel_addowner(owner_token, channel_id+100, nonowner_u_id)
    