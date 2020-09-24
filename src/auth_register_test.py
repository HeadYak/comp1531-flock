from auth import auth_register
import pytest
import echo
from error import InputError

def test_auth_register_BaseCase():
    result = auth_register('validemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')
    assert result == {
        'u_id': 1,
        'token': '12345',
    }

#Test case for attempting to register using an invalid email address
def test_auth_register_InvalidEmail():
    with pytest.raises(InputError):
        auth_register('Thisisnotanemailaddress', '123abc!@#', 'Hayden', 'Everest')


#Test case for when attempting to register with an email already used to register
def test_auth_register_ExistingEmail():
    with pytest.raises(InputError):
        auth_register('existingemail@gmail.com', '123abc!@#', 'Hayden', 'Everest')   


#Test case when attempting to register with a password shorter than 6 characters
def test_auth_register_InvalidPassword():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', 'Everest')  

#Test case for when attempting to register with a first name thats too long
def test_auth_register_InvalidFirstName1():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden'*100, 'Everest')       

#Test case for when attempting to register with a empty first name
def test_auth_register_InvalidFirstName2():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', '', 'Everest')              

#Test case for when attempting to register with a last name thats too long
def test_auth_register_InvalidLastName1():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', 'Everest'*100)      


#Test case for when attempting to register with a empty last name
def test_auth_register_InvalidLastName2():
    with pytest.raises(InputError):
        auth_register('validemail@gmail.com', '123', 'Hayden', '')   
               
