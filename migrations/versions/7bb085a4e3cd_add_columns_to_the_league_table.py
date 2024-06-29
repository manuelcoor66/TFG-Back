"""Add columns to the league table

Revision ID: 7bb085a4e3cd
Revises: 80fb8d1bb0c6
Create Date: 2024-06-29 18:44:09.188987

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7bb085a4e3cd'
down_revision: Union[str, None] = 'ee3f67057240'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('league', sa.Column('id', sa.Integer, primary_key=True))
    op.add_column('league', sa.Column('name', sa.String(100), nullable=False))
    op.add_column('league', sa.Column('description', sa.String(100)))
    op.add_column('league', sa.Column('created_by', sa.Integer))
    op.add_column('league', sa.Column('enrolments', sa.Integer))
    op.add_column('league', sa.Column('points_victory', sa.Integer, nullable=True))
    op.add_column('league', sa.Column('points_defeat', sa.Integer, nullable=True))
    op.add_column('league', sa.Column('weeks', sa.Integer, nullable=True))
    op.add_column('league', sa.Column('weeks_played', sa.Integer, nullable=True))
    op.add_column('league', sa.Column('date_start', sa.Date, nullable=True))


def downgrade():
    op.drop_column('league', 'id')
    op.drop_column('league', 'name')
    op.drop_column('league', 'description')
    op.drop_column('league', 'created_by')
    op.drop_column('league', 'enrolments')
    op.drop_column('league', 'points_victory')
    op.drop_column('league', 'points_defeat')
    op.drop_column('league', 'weeks')
    op.drop_column('league', 'weeks_played')
    op.drop_column('league', 'date_start')
