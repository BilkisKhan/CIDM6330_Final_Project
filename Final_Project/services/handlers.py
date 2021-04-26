from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

from Final_Project.domain import commands, events, models

if TYPE_CHECKING:
    from . import unit_of_work


def add_user(
    cmd: commands.AddUserCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        # look to see if we already have this user as the title is set as unique
        users = uow.users.get_by_userName(value=cmd.userName)
        # checks to see if the list is empty
        if not users:
            user = models.User(
                cmd.id, cmd.userName, cmd.password, cmd.firstName, cmd.lastName, cmd.dateofBirth, cmd.departmentName,
            )
            uow.users.add(user)
        uow.commit()


def list_users(
    cmd: commands.ListUsersCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    users = None
    with uow:
        users = uow.users.all()

    return users


# DeleteUserCommand: id: int
def delete_user(
    cmd: commands.DeleteUserCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


# EditUserCommand(Command):
def edit_user(
    cmd: commands.EditUserCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        pass


EVENT_HANDLERS = {
    events.UserAdded: [add_user],
    events.UsersListed: [list_users],
    events.UserDeleted: [delete_user],
    events.UserEdited: [edit_user],
}

COMMAND_HANDLERS = {
    commands.AddUserCommand: add_user,
    commands.ListUsersCommand: list_users,
    commands.DeleteUserCommand: delete_user,
    commands.EditUserCommand: edit_user,
}
