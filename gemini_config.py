from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel,set_tracing_disabled

set_tracing_disabled(disabled=True)

key = config('GEMINI_API_KEY')
base_url = config('GEMINI_BASE_URL')
gemini_client = AsyncOpenAI(api_key=key, base_url=base_url)

# 🧠 Define the AI model to use
GEMINI_MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", # ⚡ Using Gemini 2.5 Flash model
    openai_client=gemini_client
)
