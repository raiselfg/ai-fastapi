from openai import AsyncClient

from app.schemas.ai import AiResponse

class AiService():
    def __init__(self, ai_client: AsyncClient) -> None:
        self._ai_client = ai_client

    async def ask_llm(self, question: str) -> AiResponse:
        response = await self._ai_client.chat.completions.create(
            model="nvidia/nemotron-3.5-lightning:free",
            messages=[{"role": "user", "content": question}],
        )

        answer = response.choices[0].message.content

        if answer is None:
            raise Exception("error")

        return AiResponse(answer=answer)