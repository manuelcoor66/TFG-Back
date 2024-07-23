"""Add columns to the sports table

Revision ID: ca25a80f3a42
Revises: 5201ca6f881c
Create Date: 2024-07-23 22:03:41.699673

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ca25a80f3a42"
down_revision: Union[str, None] = "5201ca6f881c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("sports", sa.Column("id", sa.Integer, primary_key=True))
    op.add_column("sports", sa.Column("name", sa.String(length=20)))
    op.add_column("sports", sa.Column("icon", sa.String(length=20)))
    op.add_column("sports", sa.Column("players", sa.Integer))
    op.add_column("league", sa.Column("sport_id", sa.Integer))


def downgrade() -> None:
    op.drop_column("sports", "id")
    op.drop_column("sports", "name")
    op.drop_column("sports", "icon")
    op.drop_column("sports", "players")
    op.drop_column("league", "sport_id")
