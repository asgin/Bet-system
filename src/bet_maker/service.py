import asyncio
from src.bet_maker.bases import BaseService
from src.bet_maker.repository import BetRepository
from sqlalchemy.ext.asyncio import AsyncSession
import aiohttp
import logging
from src.bet_maker.schemas import Bet
from typing import Optional

class BetService(BaseService):
    def __init__(self, db: AsyncSession):
        self.repository = BetRepository(db)

    async def get_actually_events(self) -> Optional[dict]:
        async with aiohttp.ClientSession() as session:
            for attemp in range(3):
                try:
                    async with session.get('http://line_provider:8080/api/v1/events') as response:
                        if response.status == 200:
                            return await response.json()
                except Exception as e:
                    logging.warning(f'Connection error attemp {attemp + 1}, error: {e}')
                    await asyncio.sleep(1)
                logging.error("failed to get actually events from line provider")
                return None
            
    async def create(self, id: int, bet_price: float) -> int:
        id = await self.repository.create(id, bet_price)
        return id
    
    async def get_all_bets(self) -> list[Bet] | None:
        all_bets = await self.repository.get_all_bets()
        return [Bet.model_validate(bet, from_attributes=True) for bet in all_bets] if all_bets else []
    