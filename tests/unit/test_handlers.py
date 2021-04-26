from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from Final_Project import bootstrap
from Final_Project.domain import commands
from Final_Project.services import handlers, unit_of_work
from Final_Project.adapters import repository

from Final_Project.adapters.orm import start_mappers
from Final_Project.services.unit_of_work import FakeUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())


class TestAddUser:
    def test_add_user(self):

        # bus1 = bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())
        bus = boostrap_test_app()

        bus.handle(
            commands.AddUserCommand(
                f"11", f"bilkis12", f"wewe22wdA@", f"Bilkis",
                f"Khan", f"oct-12-1987", f"IT"
            )
        )
        assert bus.uow.users.get_by_userName(f"bilkis12") is not None
        assert bus.uow.committed

    def test_get_user_by_userid(self):
        bus = boostrap_test_app()

        bus.handle(
            commands.AddUserCommand(
                f"11", f"bilkis12", f"wewe22wdA@", f"Bilkis",
                f"Khan", f"oct-12-1987", f"IT"
            )
        )

        assert bus.uow.users.get_by_userid("11") is not None
        assert bus.uow.committed

    def test_get_all_users(self):
        bus = boostrap_test_app()

        bus.handle(
            commands.AddUserCommand(
                f"11", f"bilkis12", f"wewe22wdA@", f"Bilkis",
                f"Khan", f"oct-12-1987", f"IT"
            )
        )
        bus.handle(
            commands.AddUserCommand(
                f"12", f"bilkis13", f"wewe22wdA@", f"TestUser",
                f"TestUserLastName", f"oct-12-1987", f"IT"
            )
        )

        records = bus.uow.users.get_all()
        assert len(records) == 2
