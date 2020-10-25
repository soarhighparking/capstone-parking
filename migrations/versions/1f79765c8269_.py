"""empty message

Revision ID: 1f79765c8269
Revises: 7e7a003df875
Create Date: 2020-10-21 22:18:40.473120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f79765c8269'
down_revision = '7e7a003df875'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('zone', sa.Column('children', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('zone', 'children')
    # ### end Alembic commands ###