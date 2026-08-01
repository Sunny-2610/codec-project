from app.models.chat import Chat
from app.models.message import Message


class ChatService:
    def __init__(self, db) -> None:
        self.db = db

    def create_chat(self, name: str | None, chat_type: str) -> Chat:
        chat = Chat(name=name, chat_type=chat_type)
        self.db.add(chat)
        self.db.commit()
        self.db.refresh(chat)
        return chat

    def create_message(self, chat_id: int, sender_id: int, content: str) -> Message:
        message = Message(chat_id=chat_id, sender_id=sender_id, content=content)
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message
