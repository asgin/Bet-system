from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession

class BaseBetInterface(ABC):
    
    @abstractmethod
    async def get_all_bets(self, *args, **kwargs):
        raise NotImplementedError
    
    @abstractmethod
    async def create(self, *args, **kwargs):
        raise NotImplementedError
    
class BaseRepository(BaseBetInterface):
    def __init__(self, db: AsyncSession):
        self.db = db
    
class BaseService(BaseBetInterface):
    @abstractmethod
    async def get_actually_events(self, *args, **kwargs):
        raise NotImplementedError