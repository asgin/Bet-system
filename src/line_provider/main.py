from fastapi import FastAPI
from src.line_provider.router import router

app = FastAPI(title="Line Provider")
app.include_router(router)
