"""Add Second Helvetic Confession

Revision ID: 2cb636320394
Revises: d21c001d987c
Create Date: 2022-10-06 09:44:43.900613

"""
from __future__ import annotations

from itertools import chain
from pathlib import Path
from typing import TypedDict

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql
from tomli import load

from erasmus.db.confession import ConfessionType, NumberingType

# revision identifiers, used by Alembic.
revision = '2cb636320394'
down_revision = 'd21c001d987c'
branch_labels = None
depends_on = None


confessions = sa.table(
    'confessions',
    sa.column('id', sa.Integer),
    sa.column('command', sa.String),
    sa.column('name', sa.String),
    sa.column('type', postgresql.ENUM(ConfessionType, name='confession_type')),
    sa.column(
        'numbering',
        postgresql.ENUM(NumberingType, name='confession_numbering_type'),
    ),
    sa.column(
        'subsection_numbering',
        postgresql.ENUM(NumberingType, name='confession_numbering_type'),
    ),
)

confession_sections = sa.table(
    'confession_sections',
    sa.column('confession_id', sa.Integer),
    sa.column('number', sa.Integer),
    sa.column('subsection_number', sa.Integer),
    sa.column('title', sa.Text),
    sa.column('text', sa.Text),
)


class _SubSectionDict(TypedDict):
    subsection_number: int
    text: str


class _SectionDict(TypedDict):
    number: int
    title: str
    subsections: list[_SubSectionDict]


class _DataDict(TypedDict):
    title: str
    sections: list[_SectionDict]


COMMAND = 'shc'


def upgrade():
    conn = op.get_bind()

    with (
        Path(__file__).resolve().parent
        / f'{revision}_add_second_helvetic_confession.toml'
    ).open('rb') as f:
        data: _DataDict = load(f)  # type: ignore

    op.bulk_insert(
        confessions,
        [
            {
                'command': COMMAND,
                'name': data['title'],
                'type': ConfessionType.CHAPTERS,
                'numbering': NumberingType.ROMAN,
                'subsection_numbering': NumberingType.ARABIC,
            }
        ],
    )

    confession = conn.execute(
        sa.select(confessions).filter(confessions.c.command == COMMAND)
    ).fetchone()

    op.bulk_insert(
        confession_sections,
        list(
            chain.from_iterable(
                [
                    {
                        'confession_id': confession['id'],
                        'title': section['title'],
                        'number': section['number'],
                        'subsection_number': subsection['subsection_number'],
                        'text': subsection['text'],
                    }
                    for subsection in section['subsections']
                ]
                for section in data['sections']
            )
        ),
    )


def downgrade():
    conn = op.get_bind()

    confession = conn.execute(
        sa.select(confessions).filter(confessions.c.command == COMMAND)
    ).fetchone()

    op.execute(
        confession_sections.delete().filter(
            confession_sections.c.confession_id == confession['id']
        )
    )
    op.execute(confessions.delete().filter(confessions.c.id == confession['id']))
