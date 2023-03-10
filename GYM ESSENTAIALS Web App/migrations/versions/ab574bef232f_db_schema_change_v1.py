"""DB Schema Change V1

Revision ID: ab574bef232f
Revises: 
Create Date: 2022-01-31 10:06:21.998832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab574bef232f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('car', 'features')
    op.drop_column('car', 'engine')
    op.add_column('user', sa.Column('name', sa.String(length=50), nullable=False))
    op.drop_column('user', 'fname')
    op.drop_column('user', 'lname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lname', sa.VARCHAR(length=50), nullable=False))
    op.add_column('user', sa.Column('fname', sa.VARCHAR(length=50), nullable=False))
    op.drop_column('user', 'name')
    op.add_column('car', sa.Column('engine', sa.VARCHAR(length=20), nullable=False))
    op.add_column('car', sa.Column('features', sa.VARCHAR(length=500), nullable=False))
    # ### end Alembic commands ###
