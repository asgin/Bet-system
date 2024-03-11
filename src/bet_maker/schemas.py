from pydantic import BaseModel
from src.bet_maker.models import Status

class Bet(BaseModel):
    id: int
    status: Status