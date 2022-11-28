"""Add relationship of promotion tabler in product table

Revision ID: fbeb36f2b66d
Revises: 971c78c5b802
Create Date: 2022-10-10 19:43:39.375192

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fbeb36f2b66d'
down_revision = '971c78c5b802'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('promotion_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'products', 'promotion', ['promotion_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'promotion_id')
    # ### end Alembic commands ###
