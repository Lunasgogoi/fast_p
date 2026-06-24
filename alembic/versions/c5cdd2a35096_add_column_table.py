"""add_column_table

Revision ID: c5cdd2a35096
Revises: 942551cfa936
Create Date: 2026-06-24 18:03:50.550356

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5cdd2a35096'
down_revision: Union[str, Sequence[str], None] = '942551cfa936'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    
    op.drop_column('posts', 'content')
    pass
