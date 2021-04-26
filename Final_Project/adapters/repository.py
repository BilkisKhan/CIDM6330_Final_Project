from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Set

from Final_Project.adapters import orm
from Final_Project.domain.models import User


class AbstractUserRepository(ABC):
    def __init__(self):
        # seen is in reference to events detected
        self.seen = set()

    def add(self, user: User) -> None:
        # add to repo
        self._add(user)
        # add to event list
        self.seen.add(user)

    def get_all(self) -> list[User]:
        users: list[User] = self._get_all()
        if users:
            self.seen.update(users)
        return users

    def get_by_userid(self, value: int) -> User:
        # get from repo
        user: User = self._get_by_userid(value)
        if user:
            self.seen.add(user)
        return user

    def get_by_userName(self, value: str) -> User:
        # get from repo
        user: User = self._get_by_userName(value)
        if user:
            self.seen.add(user)
        return user

    @abstractmethod
    def _add(self, user: User) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _add_all(self, users: list[User]) -> None:
        raise NotImplementedError("Derived classes must implement add_all")

    @abstractmethod
    def _delete(user: User) -> None:
        raise NotImplementedError("Derived classes must implement delete")

    @abstractmethod
    def _get_all(self) -> list[User]:
        raise NotImplementedError("Derived classes must implement get_all")

    @abstractmethod
    def _get_by_userid(self, value: int) -> User:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_by_userName(self, value: str) -> User:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _update(self, user: User) -> None:
        raise NotImplementedError("Derived classes must implement update")

    @abstractmethod
    def _update(self, users: list[User]) -> None:
        raise NotImplementedError("Derived classes must implement update")


class SqlAlchemyUserRepository(AbstractUserRepository):
    """
    Uses guidance from the basic SQLAlchemy 1.4 tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add(self, user: User) -> None:
        self.session.add(user)

    def _add_all(self, users: list[User]) -> None:
        self.session.add_all(users)

    def _delete(self, user: User) -> None:
        pass

    def _get_all(self) -> list[User]:
        return self.session.query(User).all()

    def _get_by_userid(self, value: int) -> User:
        answer = self.session.query(User).filter(User.id == value)
        return answer.one()

    def _get_by_userName(self, value: str) -> User:
        answer = self.session.query(User).filter(User.userName == value)
        return answer.one()

    def _update(self, user) -> None:
        pass

    def _update(self, users: list[User]) -> None:
        pass


class FakeUserRepository(AbstractUserRepository):
    """
    Uses a Python list to store "fake" users: https://www.w3schools.com/python/python_lists.asp
    """

    def __init__(self, users):
        super().__init__()
        self._users = set(users)

    def _add(self, user) -> None:
        self._users.add(user)

    def _add_all(self, users: list[User]) -> None:
        self._users.update(users)

    def _delete(self, user: User) -> None:
        self._users.remove(user)

    def _get_all(self) -> list[User]:
        return self._users

    # python next function: https://www.w3schools.com/python/ref_func_next.asp
    def _get_by_userid(self, value: int) -> User:
        return next((b for b in self._users if b.id == value), None)

    def _get_by_userName(self, value: str) -> User:
        return next((b for b in self._users if b.userName == value), None)

    def _update(self, user: User) -> None:
        try:
            idx = self._users.index(user)
            bm = self._users[idx]
            with user:
                bm.id = user.id
                bm.userName = user.userName
                bm.password = user.password
                bm.firstName = user.firstName
                bm.lastName = user.lastName
                bm.dateofBirth = user.dateofBirth
                bm.departmentName = user.departmentName
                bm.status = user.status

                self._users[idx] = bm
        except:
            self._users.append(user)

        return None

    def _update(self, users: list[User]) -> None:
        for inbm in users:
            self._update(inbm)
