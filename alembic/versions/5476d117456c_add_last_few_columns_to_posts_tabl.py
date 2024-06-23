"""add last few columns to posts tabl 

Revision ID: 5476d117456c
Revises: 60dc5343e8ed
Create Date: 2024-06-23 18:37:51.747546

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5476d117456c'
down_revision: Union[str, None] = '60dc5343e8ed'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
                                     'published', sa.Boolean(), 
                                     nullable=False, 
                                     server_default='TRUE'
                                     )
                  )
    
    op.add_column('posts', sa.Column(
                                     'created_at', sa.TIMESTAMP(timezone=True), 
                                     nullable=False, 
                                     server_default=sa.text('NOW()')
                                     )
                  )


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    
    pass
