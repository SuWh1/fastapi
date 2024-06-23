"""add fk to post table

Revision ID: 60dc5343e8ed
Revises: b300b204e18f
Create Date: 2024-06-23 18:31:04.513798

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '60dc5343e8ed'
down_revision: Union[str, None] = 'b300b204e18f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', 
                          source_table="posts", 
                          referent_table="users", 
                          local_cols=['owner_id'], 
                          remote_cols=['id'], 
                          ondelete="CASCADE"
                          )
    
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    
    pass
