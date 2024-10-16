"""empty message

Revision ID: 25d1e2c5f1b9
Revises: a06fc3196518
Create Date: 2024-09-27 14:14:39.975412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25d1e2c5f1b9'
down_revision = 'a06fc3196518'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
