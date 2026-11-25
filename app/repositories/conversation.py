from sqlalchemy.ext.asyncio import AsyncSession

from app.models.conversation import Conversation


class ConversationRepository:
    def __init__(self, db: AsyncSession) -> None:
        self._db = db

    def create_conversation(self, title: str) -> Conversation:
        cv = Conversation(title=title)
        self._db.add(cv)

        return cv
