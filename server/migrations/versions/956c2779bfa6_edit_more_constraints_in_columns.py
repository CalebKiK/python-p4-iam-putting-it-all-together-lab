"""Edit more constraints in columns

Revision ID: 956c2779bfa6
Revises: 83733d1bcddb
Create Date: 2024-10-10 19:20:57.224922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '956c2779bfa6'
down_revision = '83733d1bcddb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('image_url',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('recipes', schema=None) as batch_op:
        batch_op.alter_column('minutes_to_complete',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
