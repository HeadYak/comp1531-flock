import pytest
from user import user_profile_sethandle, user_profile_uploadphoto
from auth import auth_register
from other import clear
from global_data import users
from error import InputError

def test_user_profile_uploadphoto():
    # creating users 

    clear()

    user = auth_register('email1@gmail.com', 'password1', 'user1', 'userlast1')
    token = user['token']

    with pytest.raises(InputError):
        #Inavlid coordinates
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', -1,5,9,12)
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 1,-5,9,12)
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 1,5,-9,12)
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 1,5,9,-12)
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', -1,-5,-9,-12)
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', -1,-5,9,12)
        user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 0,0,-5,-5)
  
    with pytest.raises(InputError):
        #Invalid url
        user_profile_uploadphoto(token, 'https://image.shutterstock.com/image-photo/bright-spring-view-cameo-island-260nw.jpg', 0,0,50,50)
        user_profile_uploadphoto(token, '', 0,0,50,50)

    with pytest.raises(InputError):
        #image not a jpeg
        user_profile_uploadphoto(token, 'https://www.publicdomainpictures.net/pictures/320000/nahled/background-image.png', 0,0,50,50)

    #No error message should appear
    user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 6,6,60,60)
    user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 0,0,100,100)
    user_profile_uploadphoto(token, 'https://media.wired.com/photos/598e35994ab8482c0d6946e0/master/w_1024%2Cc_limit/phonepicutres-TA.jpg', 0,0,1,1)

