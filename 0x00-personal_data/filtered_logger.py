#!/usr/bin/env python3
"""
0. Regex-ing Module
"""
from typing import List
import re


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    '''
    Function to filter a message based on fields and redaction pattern.
    '''
    pattern = '|'.join([f"{field}=.*?(?={separator}|$)" for field in fields])
    return re.sub(
        pattern,
        lambda x: f"{
            x.group().split('=')[0]}={redaction}",
        message)
