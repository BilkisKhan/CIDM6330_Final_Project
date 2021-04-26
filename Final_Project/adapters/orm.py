"""
Note: this is significantly refactored to use the Imperative (a.k.a. Classical) Mappings (https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings)
That would have been common in 1.3.x and earlier.
"""
import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)

from sqlalchemy.orm import registry, mapper, relationship

from Final_Project.domain.models import User

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = MetaData()


userProfile = Table(
    "userProfile",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("userName", String(255), unique=True),
    Column("password", String(255)),
    Column("firstName", Text),
    Column("lastName", Text),
    Column("dateofBirth", Text),
    Column("departmentName", Text),
    Column("status", Text),
)


def start_mappers():
    logger.info("starting mappers")
    mapper(User, userProfile)
