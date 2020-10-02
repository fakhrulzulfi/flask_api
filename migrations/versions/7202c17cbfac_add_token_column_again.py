"""add token column again

Revision ID: 7202c17cbfac
Revises: 94bdd4941509
Create Date: 2020-08-24 12:27:39.957651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7202c17cbfac'
down_revision = '94bdd4941509'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('token', sa.String(length=200), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'token')
    # ### end Alembic commands ###
