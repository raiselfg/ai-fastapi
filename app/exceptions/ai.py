class AiError(Exception):
    pass


class AiTimeoutError(AiError):
    pass


class AiProviderError(AiError):
    pass


class NoAiResponseError(AiError):
    pass