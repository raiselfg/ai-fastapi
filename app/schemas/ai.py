from typing import Annotated

from pydantic import BaseModel, StringConstraints


class AiRequest(BaseModel):
    question: Annotated[
        str, StringConstraints(min_length=3, max_length=128, strip_whitespace=True)
    ]


class AiResponse(BaseModel):
    answer: str
