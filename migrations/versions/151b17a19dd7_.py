"""empty message

Revision ID: 151b17a19dd7
Revises: b8be8d56bb73
Create Date: 2020-10-20 20:22:03.489209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '151b17a19dd7'
down_revision = 'b8be8d56bb73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('administrator', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notifications')
    # ### end Alembic commands ###
