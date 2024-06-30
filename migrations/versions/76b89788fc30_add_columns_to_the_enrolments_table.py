"""Add columns to the enrolments table

Revision ID: 76b89788fc30
Revises: 7bb085a4e3cd
Create Date: 2024-06-29 19:35:39.593094

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "76b89788fc30"
down_revision: Union[str, None] = "7bb085a4e3cd"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("enrolments", sa.Column("id", sa.Integer, primary_key=True))
    op.add_column("enrolments", sa.Column("user_id", sa.Integer))
    op.add_column("enrolments", sa.Column("league_id", sa.Integer))
    op.add_column("enrolments", sa.Column("points", sa.Integer))
    op.add_column("enrolments", sa.Column("matches_played", sa.Integer))
    op.add_column("enrolments", sa.Column("paid", sa.Boolean))
    op.add_column("enrolments", sa.Column("active", sa.Boolean))
    op.add_column("enrolments", sa.Column("finalized", sa.Boolean))


def downgrade():
    op.drop_column("enrolments", "id")
    op.drop_column("enrolments", "user_id")
    op.drop_column("enrolments", "league_id")
    op.drop_column("enrolments", "points")
    op.drop_column("enrolments", "matches_played")
    op.drop_column("enrolments", "paid")
    op.drop_column("enrolments", "active")
    op.drop_column("enrolments", "finalized")
