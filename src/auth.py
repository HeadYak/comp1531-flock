from global_data import *
import re 
import pytest
from error import InputError
#Regex for verifying emails
regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
name_maxlen = 50
name_minlen = 1 
def auth_login(email, password):
    
    def check(email):
    
        if re.search(regex,email):
            return True
        else:
            return False
     
    # Check is email is invalid 
    if check(email) == False:
        raise InputError('Invalid Email')
    
    # Handle case where no users registered 
    if len(users) == 0:
       raise InputError('Email does not belong to a user')
    
    userFound = False
    userDetails = {}
    #  Check if entered email is registered as a user
    for user in users:
        if user['email'] == email:
            userFound = True
            userDetails = user.copy()
            # Check if entered password matches registered user's password
            if password != userDetails['password']:
                raise InputError('Entered Password is Incorrect')
            else:
                user['token'] = user['u_id']
                
            break
            
    # Raise exception if email is not registered 
    if userFound == False:
        raise InputError('Email does not belong to a user')
      
    # Return u_id and token upon successful login
    return {'u_id' : userDetails['u_id'], 'token' : userDetails['token']}

def auth_logout(token):
    
    tokenFound = False
    
    # Search for matching active token
    for user in users:
        if token == user['token']:
            # Flag that active token was found and invalidate it to log out user
            tokenFound = True
            user['token'] = -1
            break
            
    return {
        'is_success': tokenFound,
    }

    

def auth_register(email, password, name_first, name_last):
    

    
    def check(email):  
  
        # pass the regular expression 
        # and the string in search() method 
        if(re.search(regex,email)):  
            return True  
            
        else:  
            return False  
            
    #Code below checks if any users in the users dictionary and checks if input email already exists
    if (check(email) == False):
        raise InputError('Invalid Email')
    
    if (len(users) != 0):
        for user in users:
            if(user['email'] == email):
                print("error")
                raise InputError('Email already registered')
    
    #Code below checks the length of the input names against restrictions
    if(len(name_first) > name_maxlen or len(name_first) < name_minlen):
        raise InputError('Invalid First Name')

    if(len(name_last) > name_maxlen or len(name_last) < name_minlen):
        raise InputError('Invalid Last Name')
    
    #Code below checks if input email is a valid email using regex
    
    #Code below checks the length of the password
    if(len(password) < 6):
        raise InputError('Invalid password')    
    #Code below is for when all conditions are met
    
    if(check(email) == True and len(password) >= 6):
        #Create a new dictionary with data about the user
        new_user = {
            'u_id': len(users)+1,
            'name_first': name_first,
            'name_last': name_last,
            'handle_str': name_first.lower() + name_last[0],
            'email': email,
            'password': password,
            'token': len(users)+1
        }

        #A copy of the dictionary is needed otherwise it messes with the references
        new_user_copy = new_user.copy()
        
        #Append the copied dictionary onto our list of users
        users.append(new_user_copy)

       
        #Return the correct output
        return {
            'u_id': new_user_copy['u_id'],
            'token': new_user_copy['token'],
        }
