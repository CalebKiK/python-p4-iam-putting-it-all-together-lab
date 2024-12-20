"""Add user_id column

Revision ID: 86fa93dce7d7
Revises: 42f275ab15c8
Create Date: 2024-10-10 19:14:41.886404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86fa93dce7d7'
down_revision = '42f275ab15c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_recipes_user_id_users'), 'users', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_recipes_user_id_users'), type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
