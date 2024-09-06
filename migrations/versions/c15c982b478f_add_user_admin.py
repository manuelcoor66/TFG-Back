"""Add user admin

Revision ID: c15c982b478f
Revises: 8a41d214bb17
Create Date: 2024-09-04 16:46:54.405039

"""

from typing import Sequence, Union

import bcrypt
from alembic import op
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Enum

from src.utils.userEnum import UserState, UserRole


# revision identifiers, used by Alembic.
revision: str = "c15c982b478f"
down_revision: Union[str, None] = "8a41d214bb17"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

user_table = table(
    "user",
    column("name", String),
    column("last_names", String),
    column("email", String),
    column("password", String),
    column("security_word", String),
    column("matches", Integer),
    column("wins", Integer),
    column("state", Enum(UserState)),
    column("role", Enum(UserRole)),
)


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=10)
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def upgrade() -> None:
    hashed_password = hash_password("admin1234!")

    op.bulk_insert(
        user_table,
        [
            {
                "name": "admin",
                "last_names": "admin",
                "email": "admin@admin.com",
                "password": hashed_password,
                "security_word": "",
                "matches": 0,
                "wins": 0,
                "state": UserState.AVAILABLE,
                "role": UserRole.ADMIN,
            }
        ],
    )


def downgrade() -> None:
    op.execute("""DELETE FROM "user" WHERE email='admin@admin.com'""")
