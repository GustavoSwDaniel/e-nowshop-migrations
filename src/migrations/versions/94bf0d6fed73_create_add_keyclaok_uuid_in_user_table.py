"""Create add keyclaok uuid in user table

Revision ID: 94bf0d6fed73
Revises: 42d8cc5f3a4e
Create Date: 2022-08-24 17:34:53.816622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94bf0d6fed73'
down_revision = '42d8cc5f3a4e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('keycloak_uuid', sa.String(length=37), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'keycloak_uuid')
    # ### end Alembic commands ###