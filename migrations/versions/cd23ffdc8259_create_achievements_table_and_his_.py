"""Create achievements table and his columns

Revision ID: cd23ffdc8259
Revises: ca25a80f3a42
Create Date: 2024-08-06 18:11:33.570299

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "cd23ffdc8259"
down_revision: Union[str, None] = "ca25a80f3a42"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "achievements",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("description", sa.String(length=100), nullable=False, unique=True),
        sa.Column("table", sa.String(length=20), nullable=False),
        sa.Column("column", sa.String(length=20), nullable=False),
        sa.Column("amount", sa.Integer),
    )


def downgrade() -> None:
    op.drop_column("achievements", "id")
    op.drop_column("achievements", "description")
    op.drop_column("achievements", "table")
    op.drop_column("achievements", "column")
    op.drop_column("achievements", "amount")
    op.drop_table("achievements")
