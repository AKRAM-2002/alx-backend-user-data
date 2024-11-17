#!/usr/bin/env python3
'''
class Auth to the API authentication
'''
from flask import request
from typing import List, TypeVar
import os

class Auth:
    """Authentication class.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if a path requires authentication, with slash tolerance.
        Returns True if the path is not in the list of excluded_paths.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path by ensuring it ends with a '/'
        if not path.endswith('/'):
            path += '/'

        # Check if normalized path is in excluded_paths
        for excluded_path in excluded_paths:
            # Also ensure each excluded_path ends with '/' for comparison
            if not excluded_path.endswith('/'):
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request
        validate all requests to secure the API.
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Placeholder for retrieving the current user
        Currently returns None.
        """
        return None

    def session_cookie(self, request=None):
        '''Returns a cookie value from a request
        '''
        if request is not None:
            return request.cookies.get(os.getenv('SESSION_NAME'))
        return None
