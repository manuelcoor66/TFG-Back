"""Add columns to the matches table

Revision ID: 237fca53492c
Revises: 76b89788fc30
Create Date: 2024-07-09 19:19:57.141497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '237fca53492c'
down_revision: Union[str, None] = '76b89788fc30'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("matches", sa.Column("id", sa.Integer, primary_key=True))
    op.add_column("matches", sa.Column("league_id", sa.Integer))
    op.add_column("matches", sa.Column("result", sa.String(length=50)))
    op.add_column("matches", sa.Column("player_id_1", sa.Integer))
    op.add_column("matches", sa.Column("player_id_2", sa.Integer))
    op.add_column("matches", sa.Column("player_id_3", sa.Integer, default=None))
    op.add_column("matches", sa.Column("player_id_4", sa.Integer, default=None))
    op.add_column("matches", sa.Column("date", sa.DateTime))
    op.add_column("matches", sa.Column("place", sa.Integer))


def downgrade() -> None:
    op.drop_column("matches", "id")
    op.drop_column("matches", "league_id")
    op.drop_column("matches", "result")
    op.drop_column("matches", "player_id_1")
    op.drop_column("matches", "player_id_2")
    op.drop_column("matches", "player_id_3")
    op.drop_column("matches", "player_id_4")
    op.drop_column("matches", "date")
    op.drop_column("matches", "place")
