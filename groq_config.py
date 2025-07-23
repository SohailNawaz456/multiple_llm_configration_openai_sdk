from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled

set_tracing_disabled(disabled=True)

key = config('GROQ_API_KEY')
base_url = config('BASE_URL_GROQ')
gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

# 🧠 Define the AI model to use
GROQ_MODEL = OpenAIChatCompletionsModel(
    model="llama-3.3-70b-versatile",  # ⚡ Using Llama 3.3 model
    openai_client=gemini_client
)
