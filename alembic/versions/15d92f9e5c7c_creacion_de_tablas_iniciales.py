"""creacion de tablas iniciales

Revision ID: 15d92f9e5c7c
Revises: ac179e2cd8cf
Create Date: 2026-08-05 00:59:32.812857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '15d92f9e5c7c'
down_revision: Union[str, Sequence[str], None] = 'ac179e2cd8cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass