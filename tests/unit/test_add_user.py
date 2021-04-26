from datetime import date, datetime, timedelta
import random

from Final_Project.domain import events
from Final_Project.domain.models import User


def test_add_user():
    pass


def test_username_cannot_empty():
    useraData = User(f"11", f"username", f"wewe22wd", f"Bilkis",
                     f"Khan", f"Oct-12-1987", f"IT")
    print(useraData.isUserNameEmpty(useraData.userName))
    assert useraData.isUserNameEmpty(useraData.userName) is False


def test_is_password_valid():
    useraData = User(f"11", f"username", f"ssdsd11A@", f"Bilkis",
                     f"Khan", f"Oct-12-1987", f"IT")
    # print(batch._isPassword_Valid(batch.password))
    assert useraData.isPassword_Valid(useraData.password) is True
