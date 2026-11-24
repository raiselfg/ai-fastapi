from datetime import datetime
import uuid
from sqlalchemy import JSON, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import BaseModel


class Messages(BaseModel):
    __tablename__ = "messages"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    conversation_id: Mapped[uuid.UUID] = mapped_column(Uuid, ForeignKey("conversation.id", ondelete="CASCADE"))
    role: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[JSON] = mapped_column(JSON, nullable=False)
    creted_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
