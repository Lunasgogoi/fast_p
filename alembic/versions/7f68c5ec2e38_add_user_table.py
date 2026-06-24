"""add user table

Revision ID: 7f68c5ec2e38
Revises: c5cdd2a35096
Create Date: 2026-06-24 18:15:59.245202

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f68c5ec2e38'
down_revision: Union[str, Sequence[str], None] = 'c5cdd2a35096'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )
    
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
    pass
