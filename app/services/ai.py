from app.exceptions.ai import AiProviderError, AiTimeoutError, NoAiResponseError
from app.schemas.ai import AiResponse
from openai import (
    APITimeoutError,
    APIConnectionError,
    APIStatusError,
    AsyncClient
)

SYSTEM_PROMPT = """
# Роль
Ты преподаватель Python с опытом backend-разработки.

# Цель
Помогать начинающим разработчикам самостоятельно
понимать программирование.

# Правила
- Объясняй сложные концепции простыми словами.
- Используй аналогии из реальной жизни.
- Не выдавай готовые решения учебных задач.
- Объясняй причины ошибок.
- Не придумывай факты.

# Формат ответа
1. Краткое объяснение.
2. Практический пример или аналогия.
3. Вопрос для проверки понимания.
"""

class AiService:
    def __init__(self, ai_client: AsyncClient):
        self._ai_client = ai_client

    async def ask_llm(self, question: str, temperature: float) -> AiResponse:
        try:
            response = await self._ai_client.chat.completions.parse(
                model="openrouter/free",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question}
                ],
                temperature=temperature,
                response_format=AiResponse,
                extra_body={
                    "provider": {
                        "require_parameters": True
                    }
                }
            )
        except APITimeoutError as err:
            raise AiTimeoutError("LLM timeout") from err

        except APIConnectionError as err:
            raise AiProviderError("Connection failed") from err

        except APIStatusError as err:
            raise AiProviderError("Provider returned an error") from err
        
        answer = response.choices[0].message.parsed

        if not answer:
            raise NoAiResponseError("No Ai response")

        if response.model:
            print(response.model)
        
        return answer