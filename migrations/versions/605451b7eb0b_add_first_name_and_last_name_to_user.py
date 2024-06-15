"""Add first_name and last_name to User

Revision ID: 605451b7eb0b
Revises: 
Create Date: 2024-06-10 10:32:38.943593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '605451b7eb0b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=150), nullable=False))
        batch_op.add_column(sa.Column('last_name', sa.String(length=150), nullable=False))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               type_=sa.String(length=150),
               existing_nullable=False)
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.String(length=200),
               existing_nullable=False)
        batch_op.drop_column('fullname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('fullname', sa.VARCHAR(length=100), nullable=False))
        batch_op.alter_column('password',
               existing_type=sa.String(length=200),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)
        batch_op.alter_column('email',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=120),
               existing_nullable=False)
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
