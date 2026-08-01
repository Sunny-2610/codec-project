from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("chats.id"), nullable=False)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=True)
    message_type = Column(String(20), default="text")
    created_at = Column(DateTime, nullable=False)

    chat = relationship("Chat", back_populates="messages")
    sender = relationship("User", back_populates="messages")
