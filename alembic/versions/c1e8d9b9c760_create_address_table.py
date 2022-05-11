"""create address table

Revision ID: c1e8d9b9c760
Revises: 
Create Date: 2022-05-10 20:19:12.163864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1e8d9b9c760'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer, nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column("users", 'address_id')

# alembic downgrade 497ad21d87ab
# alembic upgrade -1

# alembic downgrade 2c8e65a23d17
# alembic upgrade -1

