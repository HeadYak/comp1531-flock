from channels import channels_listall
from auth import auth_register
import pytest
import echo
from error import InputError

def channels_listall_test():
    #Creating users to create channels
    token1 = auth_register("user1@gmail.com", user1pass, user1, last1).token()

    with pytest.raises(InputError):
        channels_create(token1, H*21, True)
        channels_create(token1, H*21, False)
        
    #testing if channels_create adds correct information to the channels
    #dictionary is test is channels_list_test.py and channels_listall_test.py
    
