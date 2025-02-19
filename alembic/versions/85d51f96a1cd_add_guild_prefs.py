"""Add guild_prefs

Revision ID: 85d51f96a1cd
Revises: dc5428c022bd
Create Date: 2019-08-24 17:25:03.893071

"""
from __future__ import annotations

import sqlalchemy as sa
from alembic import op

import erasmus.db.base

# revision identifiers, used by Alembic.
revision = '85d51f96a1cd'
down_revision = 'dc5428c022bd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'guild_prefs',
        sa.Column('guild_id', erasmus.db.base.Snowflake(), nullable=False),
        sa.Column('bible_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['bible_id'], ['bible_versions.id']),
        sa.PrimaryKeyConstraint('guild_id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guild_prefs')
    # ### end Alembic commands ###
