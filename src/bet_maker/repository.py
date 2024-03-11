from sqlalchemy import select
from src.bet_maker.bases import BaseRepository
from src.bet_maker.models import BetModel

class BetRepository(BaseRepository):

    async def create(self, id: int, bet_price: float) -> int:
        bet = BetModel(id=id, bet_price=bet_price)
        self.db.add(bet)
        await self.db.commit()
        await self.db.refresh(bet)
        return id
    
    async def get_all_bets(self) -> list:
        query = select(BetModel)
        res = await self.db.execute(query)
        res = res.unique().scalars().all()
        return res
    