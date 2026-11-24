from typing import Annotated, Literal

from pydantic import BaseModel, Field, StringConstraints


class AiRequest(BaseModel):
    question: Annotated[
        str, StringConstraints(min_length=3, max_length=128, strip_whitespace=True)
    ]
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)


class AiResponse(BaseModel):
    topic: str
    explanation: str
    example: str
    difficulty: Literal[
        "beginner", "intermediate", "advanced"
    ]
    key_concepts: list[str]
    control_question: str
    