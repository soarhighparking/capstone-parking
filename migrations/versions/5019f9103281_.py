"""empty message

Revision ID: 5019f9103281
Revises: 18d7b6b01e86
Create Date: 2020-10-26 21:11:19.212088

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5019f9103281'
down_revision = '18d7b6b01e86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('logs', 'notes',
               existing_type=mysql.VARCHAR(length=1500),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('logs', 'notes',
               existing_type=mysql.VARCHAR(length=1500),
               nullable=False)
    # ### end Alembic commands ###