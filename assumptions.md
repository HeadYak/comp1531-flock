# Project Assumptions

## Iteration 1

### Authorization

* auth.py - auth_registration: When a user is registered they are autimatically logged in
* auth.py - auth_registration: The defualt handle str for users is ther first name plus first letter of there last name
* auth.py - auth_registration: The u_id is equal to however many channels there are plus 1

### Channels/Channel

* channels.py - channels_create: User will automatically become a member of the channel upon creating it
* channels.py - channels_create: As only requirement for name is not more than 20 characters long, channel can have no name
*  channels.py - channels_create: The channel_id is equal to however many channels there are plus 1
* channel.py - channel_invite: User can invite people to channel, even if its private, as long as they are a member/owner
* channel.py - channel_join: Global owner refers to owner of the flockr, and has access to all channels, even private ones
* channel.py - channel_join: There is no limit on the amount of channels a user can join
* channel.py - channel_leave: When an owner of a channel leaves they are no longer an owner
* channel.py - channel_addowner: User to be added as owner does not have to already be member of the channel
* channel.py - channel_addowner: Upon being added as an owner, the user is a member of the channel
* channel.py - channels_listall: channes_listall lists all public and private channels

### Data storing

* users - users are stored in a list of dictionaries with each  with each dictionary having the following keys

user = {
            'u_id': len(users)+1,
            'name_first': name_first,
            'name_last': name_last,
            'handle_str': name_first.lower() + name_last[0],
            'email': email,
            'password': password,
            'token': len(users)+1
        }


* channels - channels is a list of dictionaries with each dictionary having the following keys

 channel = {
              'channel_id': number
              'name': string
              'is_public': boolean
              'creator': dictionary,
              'owners': list of dictionaries,
              'members': list of dictionaries,
              'messages': list of dictionaries,
           }

* Creator, owners, and members are represented by dictionaries in this form

     { 
     
        'u_id': u_id,
        'name_first': name_first,
        'name_last': name_last,
                                    
     }



