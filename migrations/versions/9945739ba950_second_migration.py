"""second  migration

Revision ID: 9945739ba950
Revises: ae1105615b31
Create Date: 2022-05-16 16:42:02.282807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9945739ba950'
down_revision = 'ae1105615b31'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('age', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'age')
    # ### end Alembic commands ###
