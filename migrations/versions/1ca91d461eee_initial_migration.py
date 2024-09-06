"""Initial migration

Revision ID: 1ca91d461eee
Revises:
Create Date: 2024-06-29 18:30:35.776789

"""

from typing import Sequence, Union

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1ca91d461eee"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("user")
    op.create_table("league")
    op.create_table("enrolments")
    op.create_table("matches")
    op.create_table("sports")


def downgrade():
    op.drop_table("user")
    op.drop_table("league")
    op.drop_table("enrolments")
    op.drop_table("matches")
    op.drop_table("sports")
