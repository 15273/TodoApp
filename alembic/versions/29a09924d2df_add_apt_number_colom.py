"""add apt number colom

Revision ID: 29a09924d2df
Revises: c1e8d9b9c760
Create Date: 2022-05-10 22:06:14.880297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29a09924d2df'
down_revision = 'c1e8d9b9c760'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_num', sa.Integer, nullable=True))


def downgrade():
   op.drop_column('address', 'apt_num')
