from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=True)
    chat_type = Column(String(20), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, nullable=False)

    owner = relationship("User", back_populates="chats")
    messages = relationship("Message", back_populates="chat")
