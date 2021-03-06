"""empty message

Revision ID: f4afdafc7851
Revises: 5b6e0c5e68ad
Create Date: 2018-07-09 13:12:21.720261

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f4afdafc7851'
down_revision = '5b6e0c5e68ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('film', sa.Column('introduction', sa.String(length=1000), nullable=False))
    op.drop_column('film', 'intro')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('film', sa.Column('intro', mysql.VARCHAR(length=64), nullable=False))
    op.drop_column('film', 'introduction')
    # ### end Alembic commands ###
