from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.conversation import ConversationRepository
from app.schemas.conversations import ConversationResponse

class ConversationService():
    def __init__(self, db: AsyncSession) -> None:
        self._db = db
        self._cv_respository = ConversationRepository(db)

    async def create_conversation(self, title: str) -> ConversationResponse:
        try:
            cv = self._cv_respository.create_conversation(title)
            await self._db.commit()
        except IntegrityError:
            await self._db.rollback()
            raise

        return ConversationResponse(id=cv.id, title=cv.title)

        