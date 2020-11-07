from helper_functions import get_u_id, create_member, resetData, \
    user_exists_persist, getUserData, getChannelData, saveChannelData, \
    channel_exists_persist, user_in_channel_persist    
from error import InputError, AccessError
import threading
import datetime
from threading import Thread 
import time
from datetime import datetime, timedelta
def standup(channel_id, token, length):
    time.sleep(length)
    channels = getChannelData()
    print("Standup start for " + str(length) + " seconds")
    

    for channel in channels:
        if channel['channel_id'] == int(channel_id):
            channel['is_standup'] == False
            channel['standup'] == []
            channel['standup_finish'] == None

    saveChannelData(channels)
    
    print("Standup finish")

    return


def standup_start(token, channel_id, length):
    channels = getChannelData()
    authorised_u_id = get_u_id(token)
    if not channel_exists_persist(channel_id):
        raise InputError('Invalid channel')

    if not user_in_channel_persist(authorised_u_id, channel_id):
        raise AccessError('User not a member of channel')

    for channel in channels:
        if channel['channel_id'] == channel_id:
            if channel['is_standup'] != False:
                raise InputError('Channel already in standup')

    thread = Thread(target=standup, args=(channel_id, token, length))
    for channel in channels:
        if channel['channel_id'] == channel_id:
            channel['is_standup'] = True

    thread.start()

    finish_time = datetime.now() + timedelta(seconds = int(length))

    unixstamp = time.mktime(finish_time.timetuple())

    for channel in channels:
        if channel['channel_id'] == channel_id:
            channel['standup_finish'] = unixstamp
            
    saveChannelData(channels)

    return {'time_finish': unixstamp}


def standup_active(token, channel_id):
    channels = getChannelData()
    authorised_u_id = get_u_id(token)

    if not channel_exists_persist(channel_id):
        raise InputError('Invalid channel')

    if not user_in_channel_persist(authorised_u_id, channel_id):
        raise AccessError('User not a member of channel')

    for channel in channels:
        if channel['channel_id'] == channel_id:
            is_active = channel['is_standup']
            time_finish = channel['standup_finish']

    return {'is_active': is_active, 'time_finish': time_finish}       