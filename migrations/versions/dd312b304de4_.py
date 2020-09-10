"""empty message

Revision ID: dd312b304de4
Revises: fc3ce30ed348
Create Date: 2020-09-10 00:57:16.167876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd312b304de4'
down_revision = 'fc3ce30ed348'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Enum('OPEN', 'RESOLVED', name='logstatus'), nullable=True),
    sa.Column('type', sa.Enum('WEBSITE', 'DATBASE', 'HARDWARE', name='logtype'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logs')
    # ### end Alembic commands ###
