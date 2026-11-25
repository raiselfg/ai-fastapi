from typing import Annotated
from pydantic import UUID4, BaseModel, StringConstraints


class ConversationRequest(BaseModel):
    title: Annotated[str, StringConstraints(min_length=3, max_length=32, strip_whitespace=True)]

class ConversationResponse(BaseModel):
    id: UUID4
    title: str
