"""Add price to league table

Revision ID: 913256ff07d4
Revises: 86ca2118fd4a
Create Date: 2024-08-15 13:42:05.949031

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "913256ff07d4"
down_revision: Union[str, None] = "86ca2118fd4a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("league", sa.Column("price", sa.Integer))


def downgrade() -> None:
    op.drop_column("league", "price")
