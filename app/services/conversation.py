from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.conversation import ConversationRepository
from app.schemas.conversations import ConversationResponse

class ConversationService():
    def __init__(self, db: AsyncSession) -> None:
        self._db = db
        self._cv_repository = ConversationRepository(db)

    async def create_conversation(self, title: str) -> ConversationResponse:
        async with self._db.begin():
            cv = self._cv_repository.create_conversation(title)

        return ConversationResponse(id=cv.id, title=cv.title)

        