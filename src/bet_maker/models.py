from src.bet_maker.database import Base
from sqlalchemy.orm import Mapped, mapped_column
import enum

class Status(enum.Enum):
    NEW = "New"
    WIN = "Win"
    LOSS = "Loss"

class BetModel(Base):
    __tablename__ = 'bets'
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bet_price: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(nullable=False, default=Status.NEW)
