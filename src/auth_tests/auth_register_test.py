import sys
sys.path.append("..")

from auth import auth_register, users
import pytest
from error import InputError
from other import clear
# from global_data import users


#Test below is not a implementation of black_box testing

# def test_auth_register_BaseCase():
#     clear()
#     result1 = auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton')
#     u_id1 = result1['u_id']
#     print(u_id1)
    
#     result = auth_register('avalidemail@gmail.com', '123abc!@#*', 'Hayden', 'Everest')
#     u_id = result['u_id']
#     print(u_id)
#     token = result['token']
#     for user in users:
#         if(user['u_id'] == u_id and user['token'] == token):
#             pass

#     clear()
def test_auth_register_BaseCase():
    clear()
    auth_register('anothervalidemail@gmail.com', '123abc!@#*', 'Howard', 'Everton')
    print(users)
    assert(len(users) == 1)
    print(users)
    auth_register('andanothervalidemail@gmail.com', '123abc!@#*', 'Hayden', 'Everest')

    assert(len(users) == 2)
    clear()
    pass

    
#Test case for attempting to register using an invalid email address
def test_auth_register_InvalidEmail():
    with pytest.raises(InputError):
        auth_register('Thisisnotanemailaddress', '123abc!@#', 'Hayden', 'Everest')
    clear()

#Test case for when attempting to register with an email already used to register
def test_auth_register_ExistingEmail():
    auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123abc!@#', 'Howard', 'Evererton')
        auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')

    clear()
         


#Test case when attempting to register with a password shorter than 6 characters
def test_auth_register_InvalidPassword():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', 'Everest')  

    clear()

#Test case for when attempting to register with a first name thats too long
def test_auth_register_InvalidFirstName1():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden'*100, 'Everest') 
    
    clear()

#Test case for when attempting to register with a empty first name
def test_auth_register_InvalidFirstName2():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', '', 'Everest')      

    clear()

#Test case for when attempting to register with a last name thats too long
def test_auth_register_InvalidLastName1():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', 'Everest'*100)
    
    clear()


#Test case for when attempting to register with a empty last name
def test_auth_register_InvalidLastName2():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', '') 

    clear()
               
