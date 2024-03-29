"""initial

Revision ID: e67e14089304
Revises: 
Create Date: 2024-03-10 13:17:16.415730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e67e14089304'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bet_price', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('NEW', 'WIN', 'LOSS', name='status'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bets_id'), 'bets', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_bets_id'), table_name='bets')
    op.drop_table('bets')
    # ### end Alembic commands ###
