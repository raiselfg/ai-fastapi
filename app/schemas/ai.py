from pydantic import BaseModel

class AiRequest(BaseModel):
    question: str

class AiResponse(BaseModel):
    answer: str