
from app.config.ai import ai_client
from app.config.settings import Settings


class Ai_Service():
    def __init__(self, settings: Settings) -> None:
        self._setings = settings

    async def ask_llm(self, text: str) -> str:
        response = await ai_client.chat.completions.create(
            model="nvidia/nemotron-3.5-lightning:free",
            messages=[{"role": "user", "content": text}],
        )

        answer = response.choices[0].message.content

        if answer is None:
            raise Exception("error")
        
        return answer