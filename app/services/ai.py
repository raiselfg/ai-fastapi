from app.exceptions.ai import AiProviderError, AiTimeoutError, NoAiResponseError
from app.schemas.ai import AiResponse
from openai import (
    APITimeoutError,
    APIConnectionError,
    APIStatusError,
    AsyncClient
)

class AiService:
    def __init__(self, ai_client: AsyncClient) -> None:
        self._ai_client = ai_client

    async def ask_llm(self, question: str) -> AiResponse:
        try:
            response = await self._ai_client.chat.completions.create(
                model="nvidia/nemotron-3.5-lightning:free",
                messages=[{"role": "user", "content": question}],
            )
        except APITimeoutError as err:
            raise AiTimeoutError("LLM timeout") from err

        except APIConnectionError as err:
            raise AiProviderError("Connection failed") from err

        except APIStatusError as err:
            raise AiProviderError("Provider returned an error") from err
        
        answer = response.choices[0].message.content

        if not answer or not answer.strip():
            raise NoAiResponseError("no ai response")

        return AiResponse(answer=answer)