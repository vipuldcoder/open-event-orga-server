"""empty message

Revision ID: f55fde3d62b1
Revises: 00ea66754d06
Create Date: 2016-06-14 16:35:37.817737

"""

# revision identifiers, used by Alembic.
revision = 'f55fde3d62b1'
down_revision = '00ea66754d06'

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('topic', sa.String(), nullable=True))
    op.add_column('events', sa.Column('type', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'type')
    op.drop_column('events', 'topic')
    ### end Alembic commands ###
