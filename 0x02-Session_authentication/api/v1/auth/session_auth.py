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
import uuid


class SessionAuth(Auth):
    """class BasicAuth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''Creates a Session ID for a user_id
        '''
        if type(user_id) is str:
            id_session = str(uuid.uuid4())
            self.user_id_by_session_id[id_session] = user_id
            return id_session

        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''Returns a User ID based on session id
        '''
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
