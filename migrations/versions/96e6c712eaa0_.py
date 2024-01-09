"""empty message

Revision ID: 96e6c712eaa0
Revises: 32c26ca62fe9
Create Date: 2024-01-08 16:35:40.296123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96e6c712eaa0'
down_revision = '32c26ca62fe9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('invoice')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoice',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('amount_due', sa.FLOAT(), nullable=True),
    sa.Column('payment_status', sa.VARCHAR(length=20), nullable=True),
    sa.Column('issued_date', sa.DATE(), nullable=True),
    sa.Column('due_date', sa.DATE(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.Column('updated_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
