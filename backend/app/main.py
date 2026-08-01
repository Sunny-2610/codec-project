from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import auth, chats, websocket
from app.core.config import settings
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Real-Time Chat API",
    description="Production-ready chat application API built with FastAPI and WebSockets",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["authentication"])
app.include_router(chats.router, prefix="/api/v1/chats", tags=["chats"])
app.include_router(websocket.router, prefix="/ws", tags=["websocket"])


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
