import pytest
import re
from subprocess import Popen, PIPE
import signal
from time import sleep
import requests
import json

def test_auth_register_http(url):
    '''
    A simple test to check echo
    '''
    resp = requests.post(url + 'auth/register', params={'email': 'hello@gmail.com', 'password' : 'HelloPassword!', 'name_first' : 'Frank' , 'name_last' : 'Su'})
    assert json.loads(resp.text) == {'email': 'hello@gmail.com', 'password' : 'HelloPassword!', 'name_first' : 'Frank' , 'name_last' : 'Su'}