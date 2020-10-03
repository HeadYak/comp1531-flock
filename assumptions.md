# Project Assumptions

## Iteration 1

* channels.py - channels_create: User will automatically become a member of the channel upon creating it
* channels.py - channels_create: As only requirement for name is not more than 20 characters long, channel can have no name
* channel.py - channel_invite: User can invite people to channel, even if its private, as long as they are a member/owner
* channel.py - channel_join: Global owner refers to owner of the flockr, and has access to all channels, even private ones
* channel.py - channel_addowner: User to be added as owner does not have to already be member of the channel
* channel.py - channel_addowner: Upon being added as an owner, the user is a member of the channel
