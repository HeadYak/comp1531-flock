import pytest
import re
from subprocess import Popen, PIPE
import signal
from time import sleep
import requests
import json

def test_auth_login_http(url):
    '''
    A simple test to check echo
    '''
    resp = requests.post(url + 'auth/login', params={'email': 'hello@gmail.com', 'password' : 'HelloPassword!'})
    assert json.loads(resp.text) == {'email': 'hello@gmail.com', 'password' : 'HelloPassword!'}