"""create posts table

Revision ID: 942551cfa936
Revises: 
Create Date: 2026-06-24 17:55:18.598008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '942551cfa936'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        )
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    
    op.drop_table('posts')
    
    pass
