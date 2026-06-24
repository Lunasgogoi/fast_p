"""add foreign key to posts table

Revision ID: 24ef7d8b6d0c
Revises: 7f68c5ec2e38
Create Date: 2026-06-24 18:22:26.008444

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = "24ef7d8b6d0c"
down_revision: Union[str, Sequence[str], None] = "7f68c5ec2e38"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "post_users_fk", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE"
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("post_users_fk", "posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")
    pass
