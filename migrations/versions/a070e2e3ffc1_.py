"""empty message

Revision ID: a070e2e3ffc1
Revises: f619500c0baa
Create Date: 2021-04-01 02:48:46.355221

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a070e2e3ffc1'
down_revision = 'f619500c0baa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetfavorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planetid', sa.Integer(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planetid'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planetfavorite')
    # ### end Alembic commands ###
