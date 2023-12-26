"""refill

Revision ID: ee5e0a1a5bea
Revises: 48a138880204
Create Date: 2023-12-08 11:37:46.573628

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ee5e0a1a5bea"
down_revision: Union[str, None] = "48a138880204"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "groups",
        sa.Column("pk", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=250), nullable=False),
        sa.PrimaryKeyConstraint("pk"),
    )
    op.create_table(
        "subjects",
        sa.Column("pk", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=250), nullable=False),
        sa.PrimaryKeyConstraint("pk"),
    )
    op.create_table(
        "students",
        sa.Column("pk", sa.Integer(), nullable=False),
        sa.Column("f_name", sa.String(length=250), nullable=False),
        sa.Column("l_name", sa.String(length=250), nullable=False),
        sa.Column("stud_group", sa.SmallInteger(), nullable=False),
        sa.ForeignKeyConstraint(
            ["stud_group"],
            ["groups.pk"],
        ),
        sa.PrimaryKeyConstraint("pk"),
    )
    op.create_table(
        "teachers",
        sa.Column("pk", sa.Integer(), nullable=False),
        sa.Column("f_name", sa.String(length=250), nullable=False),
        sa.Column("l_name", sa.String(length=250), nullable=False),
        sa.Column("subject", sa.SmallInteger(), nullable=True),
        sa.ForeignKeyConstraint(
            ["subject"],
            ["subjects.pk"],
        ),
        sa.PrimaryKeyConstraint("pk"),
    )
    op.create_table(
        "grades",
        sa.Column("pk", sa.Integer(), nullable=False),
        sa.Column("grade", sa.Integer(), nullable=True),
        sa.Column("student_pk", sa.SmallInteger(), nullable=True),
        sa.Column("class_pk", sa.SmallInteger(), nullable=True),
        sa.Column("teacher_pk", sa.SmallInteger(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["class_pk"],
            ["subjects.pk"],
        ),
        sa.ForeignKeyConstraint(
            ["student_pk"],
            ["students.pk"],
        ),
        sa.ForeignKeyConstraint(
            ["teacher_pk"],
            ["teachers.pk"],
        ),
        sa.PrimaryKeyConstraint("pk"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("grades")
    op.drop_table("teachers")
    op.drop_table("students")
    op.drop_table("subjects")
    op.drop_table("groups")
    # ### end Alembic commands ###
