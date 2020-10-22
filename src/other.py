from global_data import users, channels
from helper_functions import get_u_id, create_member, resetData
def clear():
    resetData()
    del users[:]
    del channels[:]
    pass

def users_all(token):
    return {
        'users': [
            {
                'u_id': 1,
                'email': 'cs1531@cse.unsw.edu.au',
                'name_first': 'Hayden',
                'name_last': 'Jacobs',
                'handle_str': 'hjacobs',
            },
        ],
    }

def admin_userpermission_change(token, u_id, permission_id):
    pass

def search(token, query_str):
    '''
    Function finds matching strings to the one given and returns them, 
    only if the user is a member of the channel the message is in
    '''

    message_matches = []

    member = create_member(get_u_id(token))

    for channel in channels:
        if member in channel['members']:
            for msg in channel['messages']:
                if query_str in msg['message']:
                    message_matches.append(msg)

    return message_matches
