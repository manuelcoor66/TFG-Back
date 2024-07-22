"""Create place table

Revision ID: 5201ca6f881c
Revises: 237fca53492c
Create Date: 2024-07-16 18:50:09.109876

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5201ca6f881c'
down_revision: Union[str, None] = '237fca53492c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'places',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nombre', sa.String(length=50), nullable=False),
        sa.Column('coordenadas', sa.String(length=255), nullable=False)
    )


def downgrade() -> None:
    op.drop_column("places", "id")
    op.drop_column("places", "nombre")
    op.drop_column("places", "coordenadas")
    op.drop_table('places')
