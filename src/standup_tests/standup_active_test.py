import sys
sys.path.append("..")

from auth import auth_register
from channels import channels_create
from global_data import channels
from error import InputError
from other import clear
from standup import standup_start
from helper_functions import getChannelData
import pytest