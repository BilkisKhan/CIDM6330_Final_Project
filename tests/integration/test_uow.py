import threading
import time
import traceback
from datetime import datetime, timezone
from typing import List
from unittest.mock import Mock
import pytest
from Final_Project.domain.models import User
from Final_Project.services import unit_of_work

pytestmark = pytest.mark.usefixtures("mappers")


def insert_AddUser(session, userName: str, password: str, firstName: str, lastName: str, dateofBirth: str, departmentName: str):
    session.execute(
        """
        INSERT INTO userProfile (userName, password, firstName, lastName, dateofBirth, departmentName) 
        VALUES (:userName, :password, :firstName, :lastName, :dateofBirth, :departmentName) 
        """,
        dict(
            userName=userName,
            password=password,
            firstName=firstName,
            lastName=lastName,
            dateofBirth=dateofBirth,
            departmentName=departmentName

        ),
    )


def test_can_retreive_user(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_AddUser(session, f"bilkis1234", f"wewe22wdA@",
                   f"Bilkis", f"Khan", nu.isoformat(), f"IT")
    session.commit()

    user: User = None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        user = uow.users.get_by_userName(f"bilkis1234")
        assert user.userName == f"bilkis1234"
        # uow.commit()

    # assert user.title == f"Test"
