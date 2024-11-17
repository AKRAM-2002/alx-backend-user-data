#!/usr/bin/env python3
'''
Session authentication module for the API.
'''
import re
import base64
import binascii
from typing import Tuple, TypeVar
from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    """class BasicAuth
    """
    