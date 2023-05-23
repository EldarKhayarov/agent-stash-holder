from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6bc588e34751"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "stash_request",
        sa.Column("agent_id", sa.String(), nullable=False),
        sa.Column(
            "created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("agent_id", "created_at"),
    )


def downgrade() -> None:
    op.drop_table("stash_request")
