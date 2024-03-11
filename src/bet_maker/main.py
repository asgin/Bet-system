from fastapi import FastAPI
from src.bet_maker.router import router

app = FastAPI(title="Bet Maker")
app.include_router(router)