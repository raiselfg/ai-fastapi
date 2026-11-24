from fastapi import Request
from fastapi.responses import JSONResponse

async def ai_timeout_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    return JSONResponse(
        status_code=504,
        content={"detail": "AI provider timeout"},
    )