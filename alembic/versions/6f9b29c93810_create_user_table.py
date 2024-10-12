"""create user table

Revision ID: 6f9b29c93810
Revises: 
Create Date: 2024-10-12 10:15:11.755428

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f9b29c93810'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('tg_user_id', sa.Integer, primary_key=True),
        sa.Column('role', sa.String(10), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('user')
