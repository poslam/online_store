"""add pickpoint_id to order

Revision ID: 4c17d0ef134d
Revises: bc3e9c6b291a
Create Date: 2024-01-08 13:44:55.241293

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4c17d0ef134d"
down_revision = "bc3e9c6b291a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "order",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("sum", sa.Integer(), nullable=True),
        sa.Column("time", sa.TIMESTAMP(), nullable=True),
        sa.Column("pickpoint_id", sa.Integer(), nullable=True),
        sa.Column(
            "status",
            sa.Enum("cancelled", "pending", "delivery", "done", name="orderstatuses"),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["pickpoint_id"],
            ["pickpoint.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["product.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["client.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("order")
    # ### end Alembic commands ###
