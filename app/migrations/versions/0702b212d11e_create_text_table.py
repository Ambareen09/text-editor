"""Create text table

Revision ID: 0702b212d11e
Revises: 
Create Date: 2023-06-16 00:03:36.238415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0702b212d11e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('text',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('books')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('pages_num', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('review', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('date_added', sa.DATE(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='books_pkey')
    )
    op.drop_table('text')
    # ### end Alembic commands ###
