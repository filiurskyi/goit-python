"""table rename

Revision ID: 582e4323587d
Revises: 85c8d880202a
Create Date: 2023-12-08 11:26:26.345652

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "582e4323587d"
down_revision: Union[str, None] = "85c8d880202a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("teachers", sa.Column("subject", sa.SmallInteger(), nullable=True))
    op.drop_constraint("teachers_subjects_fkey", "teachers", type_="foreignkey")
    op.create_foreign_key(None, "teachers", "subjects", ["subject"], ["pk"])
    op.drop_column("teachers", "subjects")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "teachers",
        sa.Column("subjects", sa.SMALLINT(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "teachers", type_="foreignkey")
    op.create_foreign_key(
        "teachers_subjects_fkey", "teachers", "subjects", ["subjects"], ["pk"]
    )
    op.drop_column("teachers", "subject")
    # ### end Alembic commands ###
