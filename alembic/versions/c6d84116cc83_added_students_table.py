"""added students table

Revision ID: c6d84116cc83
Revises: 
Create Date: 2025-01-05 23:40:34.685211

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6d84116cc83'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('index_number', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('pesel', sa.String(), nullable=False),
    sa.Column('gender', sa.Integer(), nullable=False),
    sa.Column('address_city', sa.String(), nullable=False),
    sa.Column('address_street', sa.String(), nullable=False),
    sa.Column('address_zipcode', sa.String(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('index_number')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###
