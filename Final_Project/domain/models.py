from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional


class User:

    def __init__(self, id: int, userName: str, password: str, firstName: str, lastName: datetime, dateofBirth: datetime, departmentName: str,):
        self.id = id
        self.userName = userName
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.dateofBirth = dateofBirth
        self.departmentName = departmentName
        self.events = []
        self._isUserNameEmpty = set()  # type: Set[OrderLine]
        self._isPassword_Valid = bool

    def isUserNameEmpty(self, userName: userName) -> bool:
        return not (userName and userName.strip())

    def isPassword_Valid(self, passwd: password) -> bool:

        SpecialSym = ['$', '@', '#', '%']
        val = True

        if len(passwd) < 6:
            print('length should be at least 6')
            val = False

        if len(passwd) > 20:
            print('length should be not be greater than 8')
            val = False

        if not any(char.isdigit() for char in passwd):
            print('Password should have at least one numeral')
            val = False

        if not any(char.isupper() for char in passwd):
            print('Password should have at least one uppercase letter')
            val = False

        if not any(char.islower() for char in passwd):
            print('Password should have at least one lowercase letter')
            val = False

        if not any(char in SpecialSym for char in passwd):
            print('Password should have at least one of the symbols $@#')
            val = False
        if val:
            return val
