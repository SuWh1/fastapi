"""add content column to posts table

Revision ID: 25f9f2745a7c
Revises: 09fcb8941c55
Create Date: 2024-06-22 00:17:34.839583

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '25f9f2745a7c'
down_revision: Union[str, None] = '09fcb8941c55'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    
    pass
