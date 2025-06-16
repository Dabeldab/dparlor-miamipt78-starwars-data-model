"""empty message

Revision ID: ce40fac824b4
Revises: ed3b003a92c6
Create Date: 2025-06-16 01:52:20.294335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce40fac824b4'
down_revision = 'ed3b003a92c6'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        'films',
        'episode_id',
        existing_type=sa.String(length=120),
        type_=sa.Integer(),
        nullable=True,
        postgresql_using='episode_id::integer'  # <-- the key line!
    )

def downgrade():
    op.alter_column(
        'films',
        'episode_id',
        existing_type=sa.Integer(),
        type_=sa.String(length=120),
        nullable=True
    )