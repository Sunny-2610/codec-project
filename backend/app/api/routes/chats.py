from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.chat import Chat
from app.models.message import Message
from app.models.user import User
from app.schemas.chat import ChatCreate, MessageCreate

router = APIRouter()


@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_chat(chat_in: ChatCreate, db: Session = Depends(get_db)):
    chat = Chat(name=chat_in.name, chat_type=chat_in.chat_type, created_at=datetime.utcnow())
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return {"id": chat.id, "name": chat.name, "chat_type": chat.chat_type}


@router.get("", response_model=list[dict])
def list_chats(db: Session = Depends(get_db)):
    chats = db.query(Chat).all()
    return [{"id": chat.id, "name": chat.name, "chat_type": chat.chat_type} for chat in chats]


@router.post("/messages", response_model=dict)
def create_message(message_in: MessageCreate, db: Session = Depends(get_db)):
    chat = db.query(Chat).filter(Chat.id == message_in.chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    sender = db.query(User).first()
    message = Message(chat_id=chat.id, sender_id=sender.id, content=message_in.content, created_at=datetime.utcnow())
    db.add(message)
    db.commit()
    db.refresh(message)
    return {"id": message.id, "content": message.content, "chat_id": message.chat_id}
