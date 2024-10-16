"""init

Revision ID: 53aeed0347c2
Revises: 
Create Date: 2024-10-13 22:54:28.378234

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53aeed0347c2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('school_emails',
    sa.Column('school_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_index(op.f('ix_school_emails_email'), 'school_emails', ['email'], unique=True)
    op.create_index(op.f('ix_school_emails_school_name'), 'school_emails', ['school_name'], unique=True)
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_name', sa.String(), nullable=True),
    sa.Column('school_name', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_teachers_id'), 'teachers', ['id'], unique=False)
    op.create_index(op.f('ix_teachers_school_name'), 'teachers', ['school_name'], unique=False)
    op.create_table('users',
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('email')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_teachers_school_name'), table_name='teachers')
    op.drop_index(op.f('ix_teachers_id'), table_name='teachers')
    op.drop_table('teachers')
    op.drop_index(op.f('ix_school_emails_school_name'), table_name='school_emails')
    op.drop_index(op.f('ix_school_emails_email'), table_name='school_emails')
    op.drop_table('school_emails')
    # ### end Alembic commands ###
