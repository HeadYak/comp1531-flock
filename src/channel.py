'''
Nessacary imports
'''
from global_data import channels
from error import InputError, AccessError
from helper_functions import user_in_channel, user_exists, channel_exists, \
    create_member, get_u_id, user_is_owner, user_is_creator, saveChannelData, \
    getChannelData, user_in_channel_persist, channel_exists_persist, user_exists_persist,\
    getUserData

#function adds user to channel
def channel_invite(token, channel_id, u_id):
    channels = getChannelData()

    '''
    Tests channel_invite function
    '''
    #retireving u_id from token from token
    authorised_u_id = get_u_id(token)

    #raising error if channel does not exist
    if not channel_exists_persist(channel_id):
        raise InputError('Invalid channel')

    #raising error is user does not exist
    if not user_exists_persist(u_id):
        raise InputError('Invalid user id')

    #raising error is user in now in channel
    if not user_in_channel_persist(authorised_u_id, channel_id):
        raise AccessError('User not a member of channel')

    #finding the correct channel then and appending new user
    for channel in channels:
        if channel['channel_id'] == int(channel_id):
            channel['members'].append(create_member(int(u_id)))
            
            
    saveChannelData(channels)
    return {}

def channel_details(token, channel_id):
    channels = getChannelData()
    '''
    Returns the details of the channel
    '''
    channel_id = int(channel_id)
    u_id = get_u_id(token)
    if not channel_exists_persist(int(channel_id)):
        raise InputError('1')
    if not user_in_channel_persist(int(u_id), int(channel_id)):
        raise AccessError('2')

    for channel in channels:
        if channel['channel_id'] == int(channel_id):

            return {
                'name': channel['name'],
                'owner_members': channel['owners'],
                'all_members': channel['members']
            }
    return None

def channel_messages(token, channel_id, start):
    '''
    returns messages in channel with given index
    '''
    channel_id = int(channel_id)
    start = int(start)
    #raises error if channel does not exits
    if not channel_exists(channel_id):
        raise InputError('Invalid channel')

    #raises error is user is not in channel
    if not user_in_channel(get_u_id(token), channel_id):
        raise AccessError('User is not in channel')

   #appends the messages in given channel to new list
    all_messages = []
    for channel in channels:
        if channel['channel_id'] == channel_id:
            all_messages = channel['messages']
            break

    #sorts list accoring to time returning lasest message first in the list
    all_messages = sorted(all_messages, key=lambda k: k['time_created'], reverse=True)

    total_messages = len(all_messages)

    #raises error if start index is greating than the amount of messages in the channel
    if start > (total_messages - 1) and total_messages != 0:
        raise InputError('Invalid start value')

    end = start + 50
    current_message = start

    #appending all the messages from the channel to a new list starting from the start index given
    channel_msg = []
    while current_message < end:
        if current_message == total_messages:
            end = -1
            break
        channel_msg.append(all_messages[current_message])
        current_message += 1

    #returning messages dictionary for channel
    return {
        'messages': channel_msg,
        'start': start,
        'end': end,
    }

#function removes user from channel
def channel_leave(token, channel_id):
    '''
    removes user from channel
    '''
    authorised_u_id = get_u_id(token)
    channels = getChannelData()

    #raises error is channel does not exist
    if not channel_exists(channel_id):
        raise InputError('Invalid channel')

    #raises error is user is not a member of the channel
    if not user_in_channel(authorised_u_id, channel_id):
        raise AccessError('User not a member of channel')

    #removing member from channel
    for channel in channels:
        if channel['channel_id'] == channel_id:
            print("Channel_before:\n" , channel['members'])
            for owner in channel['owners']:
                if owner['u_id'] == authorised_u_id:
                    channel['owners'].remove(owner)
            for member in channel['members']:
                if member['u_id'] == authorised_u_id:
                    channel['members'].remove(member)
                    print("Channels_after:\n" , channel['members'])
    saveChannelData(channels)
    return {}

#function adds user to channel
def channel_join(token, channel_id):
    '''
    adds user to channel
    '''
    channel_id = int(channel_id)
    u_id = get_u_id(token)

    #rasies error if channel does not exist
    if not channel_exists(channel_id):
        raise InputError('Invalid channel')

    #Check if channel is public or private
    public = False
    for channel in channels:
        if int(channel['channel_id']) == channel_id:
            if channel['is_public']:
                public = True

    #if channel is prive error is raised
    if not public:
        raise AccessError('Private Channel')

    #adds member to channel
    for channel in channels:
        if (
                int(channel['channel_id']) == channel_id
                and create_member(u_id) not in channel['members']
        ):
            channel['members'].append(create_member(u_id))       
    return {}

def channel_addowner(token, channel_id, u_id):
    '''
    adds owner to channel
    '''
    if not channel_exists(channel_id):
        raise InputError('Invalid channel_id')
    if not user_in_channel(get_u_id(token), channel_id):
        raise AccessError('User not associated with channel')
    if user_is_owner(u_id, channel_id) or user_is_creator(u_id, channel_id):
        raise InputError('User is already owner')

    if user_in_channel(get_u_id(token), channel_id) is not None:
        for channel in channels:
            if channel['channel_id'] == channel_id:
                channel['owners'].append(create_member(u_id))

    return {
    }

def channel_removeowner(token, channel_id, u_id):
    '''
    removes owner from channel
    '''
    if not channel_exists(channel_id):
        raise InputError('Invalid channel_id')
    if not user_in_channel(get_u_id(token), channel_id):
        raise AccessError('User not associated with channel')
    if not user_is_owner(u_id, channel_id) and not user_is_creator(u_id, channel_id):
        raise InputError('User is not owner')
    if user_in_channel(get_u_id(token), channel_id) is not None:
        for channel in channels:
            if channel['channel_id'] == channel_id:
                channel['owners'].remove(create_member(u_id))
    return {
    }
