"""Add role and state to user

Revision ID: 8a41d214bb17
Revises: 913256ff07d4
Create Date: 2024-08-24 17:08:38.223526

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM
from enum import Enum

# revision identifiers, used by Alembic.
revision: str = "8a41d214bb17"
down_revision: Union[str, None] = "913256ff07d4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class UserState(Enum):
    AVAILABLE = "AVAILABLE"
    BANNED = "BANNED"


class UserRole(Enum):
    USER = "USER"
    LEAGUEADMIN = "LEAGUEADMIN"
    ADMIN = "ADMIN"


user_state_enum = ENUM(UserState, name="userstate", create_type=False)
user_role_enum = ENUM(UserRole, name="userrole", create_type=False)


def upgrade() -> None:
    user_state_enum.create(op.get_bind(), checkfirst=True)
    user_role_enum.create(op.get_bind(), checkfirst=True)

    op.add_column(
        "user",
        sa.Column(
            "state",
            user_state_enum,
            nullable=False,
            server_default=sa.text("'AVAILABLE'::userstate"),
        ),
    )
    op.add_column(
        "user",
        sa.Column(
            "role",
            user_role_enum,
            nullable=False,
            server_default=sa.text("'USER'::userrole"),
        ),
    )

    op.alter_column("user", "state", server_default=None)
    op.alter_column("user", "role", server_default=None)


def downgrade() -> None:
    op.drop_column("user", "state")
    op.drop_column("user", "role")

    user_state_enum.drop(op.get_bind(), checkfirst=True)
    user_role_enum.drop(op.get_bind(), checkfirst=True)
