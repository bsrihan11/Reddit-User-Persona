from langchain_mistralai import ChatMistralAI
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_mistralai import MistralAIEmbeddings
from config import MISTRAL_API_KEY
import time


class RagLLM(ChatMistralAI):
    def __init__(self, *args, **kwargs):

        from langchain_core.rate_limiters import InMemoryRateLimiter
        rate_limiter = InMemoryRateLimiter(
            requests_per_second=0.25,
            max_bucket_size=1,
            check_every_n_seconds=0.3
            )


        super().__init__(
            model="mistral-large-latest",
            temperature=0,
            max_retries=5,
            rate_limiter=rate_limiter
        )


    def invoke(self, prompt, **kwargs):
        """
        Sends a prompt to the Mistral LLM with backoff on failure.

        Parameters:
            prompt (str): The input prompt to process.

        Returns:
            The model's response to the prompt.

        Raises:
            RuntimeError: If all retry attempts fail due to rate limits or other exceptions.
        """
        
        for attempt in range(10):
            try:
                return super().invoke(prompt, **kwargs)
            except Exception as e:
                wait_time = (2 ** (attempt+1)) * 0.5
                time.sleep(wait_time)
                
        raise RuntimeError("Max retries exceeded due to rate limit.")








