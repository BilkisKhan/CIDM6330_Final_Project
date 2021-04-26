"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass


@dataclass
class AddUserCommand(Command):
    """
    This command is a dataclass that encapsulates a bookmark
    This uses type hints: https://docs.python.org/3/library/typing.html
    """
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    dateofBirth: str
    departmentName: str


@dataclass
class ListUsersCommand(Command):
    order_by: str
    order: str


@dataclass
class DeleteUserCommand(Command):
    id: int


@dataclass
class EditUserCommand(Command):
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    dateofBirth: str
    departmentName: str
