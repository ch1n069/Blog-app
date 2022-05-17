"""Initial Migration

Revision ID: dff1c87606db
Revises: 9945739ba950
Create Date: 2022-05-17 11:59:33.364454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dff1c87606db'
down_revision = '9945739ba950'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'age')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###