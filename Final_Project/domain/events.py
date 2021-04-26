from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import User


class Event(ABC):
    pass


@dataclass
class UserAdded(Event):
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    dateofBirth: str
    departmentName: str


@dataclass
class UserEdited(Event):
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    dateofBirth: str
    departmentName: str


@dataclass
class UsersListed(Event):
    users: list[User]


@dataclass
class UserDeleted(Event):
    user: User
