from agents import Runner,RunConfig,set_default_openai_api,set_default_openai_client,set_tracing_disabled
from teacher_agent import gemini_agent, groq_agent
import rich
from gemini_config import GEMINI_MODEL,gemini_client

set_default_openai_api("chat_completions")
set_default_openai_client(gemini_client)
set_tracing_disabled(disabled=True)

result = Runner.run_sync(
    starting_agent=groq_agent,
    input="what is your model name?"  # ❓ Test question
)

# # 🧠 Extract model name
# model_name = getattr(gemini_agent.model, "model", "Unknown Model")

# # ✅ Print result with GROQ and model name
# rich.print(f"✅ ANSWER IS 🚀: {result.final_output} [bold green](Model: GEMINI - {model_name})[/]")


# 🚀 Run the agent with input and get response
# result = Runner.run_sync(
#     starting_agent=groq_agent,
#     input="what is your model name?" ,
#     run_config=RunConfig(model=GEMINI_MODEL,model_provider=gemini_client)
    
# )


# ✅ Print result with GROQ and model name
rich.print(f"✅ ANSWER IS 🚀: {result.final_output}")
