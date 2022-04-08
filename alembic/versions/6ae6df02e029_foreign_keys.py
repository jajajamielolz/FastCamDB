"""foreign_keys

Revision ID: 6ae6df02e029
Revises: c727ce31f5f7
Create Date: 2022-04-07 17:39:52.872130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "6ae6df02e029"
down_revision = "c727ce31f5f7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "camera_has_battery",
        sa.Column(
            "time_created",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "time_updated",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column("uuid", sa.String(), nullable=False),
        sa.Column("camera_uuid", sa.String(), nullable=False),
        sa.Column("battery_uuid", sa.String(), nullable=False),
        sa.ForeignKeyConstraint(
            ["battery_uuid"], ["battery.uuid"], ondelete="CASCADE"
        ),
        sa.ForeignKeyConstraint(
            ["camera_uuid"], ["camera.uuid"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.drop_table("camera_type")
    op.add_column(
        "camera", sa.Column("lens_mount_uuid", sa.String(), nullable=True)
    )
    op.add_column(
        "camera", sa.Column("manufacturer_uuid", sa.String(), nullable=True)
    )
    op.add_column(
        "camera", sa.Column("metering_uuid", sa.String(), nullable=True)
    )
    op.create_foreign_key(
        None,
        "camera",
        "lens_mount",
        ["lens_mount_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "camera",
        "metering",
        ["metering_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "camera",
        "manufacturer",
        ["manufacturer_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.add_column(
        "lens", sa.Column("lens_mount_uuid", sa.String(), nullable=True)
    )
    op.add_column(
        "lens", sa.Column("manufacturer_uuid", sa.String(), nullable=True)
    )
    op.create_foreign_key(
        None,
        "lens",
        "manufacturer",
        ["manufacturer_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )
    op.create_foreign_key(
        None,
        "lens",
        "lens_mount",
        ["lens_mount_uuid"],
        ["uuid"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "lens", type_="foreignkey")
    op.drop_constraint(None, "lens", type_="foreignkey")
    op.drop_column("lens", "manufacturer_uuid")
    op.drop_column("lens", "lens_mount_uuid")
    op.drop_constraint(None, "camera", type_="foreignkey")
    op.drop_constraint(None, "camera", type_="foreignkey")
    op.drop_constraint(None, "camera", type_="foreignkey")
    op.drop_column("camera", "metering_uuid")
    op.drop_column("camera", "manufacturer_uuid")
    op.drop_column("camera", "lens_mount_uuid")
    op.create_table(
        "camera_type",
        sa.Column(
            "time_created",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column(
            "time_updated",
            postgresql.TIMESTAMP(timezone=True),
            server_default=sa.text("now()"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("uuid", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("uuid", name="camera_type_pkey"),
    )
    op.drop_table("camera_has_battery")
    # ### end Alembic commands ###
