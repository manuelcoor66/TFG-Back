"""Create ticket table and his columns

Revision ID: 86ca2118fd4a
Revises: cd23ffdc8259
Create Date: 2024-08-08 18:15:09.757427

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.utils.ticketEnum import TicketState

# revision identifiers, used by Alembic.
revision: str = '86ca2118fd4a'
down_revision: Union[str, None] = 'cd23ffdc8259'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "ticket",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("league_id", sa.Integer, nullable=False),
        sa.Column("user_id", sa.Integer, nullable=False),
        sa.Column("state", sa.Enum(TicketState), nullable=False),
        sa.Column("date", sa.Date, nullable=False),
    )


def downgrade() -> None:
    op.drop_column("ticket", "id")
    op.drop_column("ticket", "league_id")
    op.drop_column("ticket", "user_id")
    op.drop_column("ticket", "state")
    op.drop_column("ticket", "date")
    op.drop_table("ticket")
    op.execute("DROP TYPE IF EXISTS ticketstate")
