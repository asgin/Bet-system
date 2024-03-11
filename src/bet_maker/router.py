from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from src.bet_maker.service import BetService
from sqlalchemy.ext.asyncio import AsyncSession
from src.bet_maker.database import get_db

router = APIRouter(prefix="/api/v1")

@router.get("/events", status_code=status.HTTP_200_OK)
async def get_actually_events(db: AsyncSession = Depends(get_db)) -> JSONResponse:
    service = BetService(db)
    res = await service.get_actually_events()
    if res is None:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to get events, pls try again")
    return JSONResponse(content=res, status_code=status.HTTP_200_OK)

@router.post("/bet", status_code=status.HTTP_201_CREATED)
async def create_bet(id: int, bet_price: float, db: AsyncSession = Depends(get_db)) -> JSONResponse:
    service = BetService(db)
    return JSONResponse(content=await service.create(id, bet_price), status_code=status.HTTP_201_CREATED)

@router.get("/bets", status_code=status.HTTP_200_OK)
async def get_all_bets(db: AsyncSession = Depends(get_db)):
    service = BetService(db)
    return await service.get_all_bets()
