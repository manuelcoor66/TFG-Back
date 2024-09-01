"""Create ticket table and its columns

Revision ID: 86ca2118fd4a
Revises: cd23ffdc8259
Create Date: 2024-08-08 18:15:09.757427

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM
from enum import Enum


class TicketState(Enum):
    OPEN = "open"
    CLOSED = "closed"
    PENDING = "pending"


ticket_state_enum = ENUM(
    "open", "closed", "pending", name="ticketstate", create_type=False
)

# revision identifiers, used by Alembic.
revision: str = "86ca2118fd4a"
down_revision: Union[str, None] = "cd23ffdc8259"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    ticket_state_enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "ticket",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("league_id", sa.Integer, nullable=False),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("state", ticket_state_enum, nullable=False),
        sa.Column("date", sa.Date, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("ticket")

    ticket_state_enum.drop(op.get_bind(), checkfirst=True)
