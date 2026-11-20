from openai import AsyncClient

from app.schemas.ai import AiResponse


class NoAiResponseError(Exception):
    pass


class NetworkAiNetworkError(Exception):
    pass


class AiService:
    def __init__(self, ai_client: AsyncClient) -> None:
        self._ai_client = ai_client

    async def ask_llm(self, question: str) -> AiResponse:
        try:
            response = await self._ai_client.chat.completions.create(
                model="nvidia/nemotron-3.5-lightning:free",
                messages=[{"role": "user", "content": question}],
            )
            answer = response.choices[0].message.content

            if answer is None:
                raise NoAiResponseError("no ai response")

            return AiResponse(answer=answer)
        except Exception as err:
            raise NetworkAiNetworkError("network error") from err
