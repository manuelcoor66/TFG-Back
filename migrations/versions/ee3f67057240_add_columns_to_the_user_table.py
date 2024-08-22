"""Add columns to the user table

Revision ID: ee3f67057240
Revises: 1ca91d461eee
Create Date: 2024-06-29 18:40:32.575263

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ee3f67057240"
down_revision: Union[str, None] = "1ca91d461eee"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("user", sa.Column("name", sa.String(length=50)))
    op.add_column("user", sa.Column("last_names", sa.String(length=50)))
    op.add_column("user", sa.Column("email", sa.String(length=50), unique=True))
    op.add_column("user", sa.Column("password", sa.String(length=200)))
    op.add_column("user", sa.Column("security_word", sa.String(length=50)))
    op.add_column("user", sa.Column("matches", sa.Integer))
    op.add_column("user", sa.Column("wins", sa.Integer))


def downgrade():
    op.drop_column("user", "name")
    op.drop_column("user", "last_names")
    op.drop_column("user", "email")
    op.drop_column("user", "password")
    op.drop_column("user", "security_word")
    op.drop_column("user", "matches")
    op.drop_column("user", "wins")
