"""Recreate Materials Table

Revision ID: bc3d4c5e556b
Revises: b20a921671b8
Create Date: 2024-01-29 22:14:22.177120

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'bc3d4c5e556b'
down_revision: Union[str, None] = 'b20a921671b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('materials',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('formula', sa.String(), nullable=False),
    sa.Column('density', sa.Float(), nullable=False),
    sa.Column('elements', postgresql.ARRAY(sa.String()), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('materials')
    # ### end Alembic commands ###