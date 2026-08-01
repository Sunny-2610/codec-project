from pydantic import BaseModel


class ChatCreate(BaseModel):
    name: str | None = None
    chat_type: str = "private"


class MessageCreate(BaseModel):
    content: str
    chat_id: int
