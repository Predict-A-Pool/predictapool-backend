"""ID is a UUID, not an int

Revision ID: ca61e2d76f00
Revises: ff74aa0ec187
Create Date: 2026-02-04 01:28:44.068905

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'ca61e2d76f00'
down_revision: Union[str, Sequence[str], None] = 'ff74aa0ec187'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Drop the existing default
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN id DROP DEFAULT
        """
    )

    # 2. Change column type with explicit cast
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN id
        TYPE UUID
        USING id::uuid
        """
    )

    op.execute('CREATE EXTENSION IF NOT EXISTS "pgcrypto"')

    # 3. Add a proper UUID default
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN id
        SET DEFAULT gen_random_uuid()
        """
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN id DROP DEFAULT
        """
    )
    op.execute(
        """
        ALTER TABLE users
        ALTER COLUMN id TYPE VARCHAR
        """
    )
