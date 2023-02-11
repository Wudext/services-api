"""Fix

Revision ID: 90c1cd8216b5
Revises: 28d38f9e2e65
Create Date: 2023-02-10 11:51:48.015134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90c1cd8216b5'
down_revision = '28d38f9e2e65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('button',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('order', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('icon', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('button')
    op.drop_table('category')
    # ### end Alembic commands ###
