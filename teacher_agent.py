
from agents import Agent
from gemini_config import config, GEMINI_MODEL
from groq_config import config, GROQ_MODEL


gemini_agent = Agent(
    name="🤖 sohail lal", 
    instructions="you are a help full assistant",

    model=GEMINI_MODEL  # 🔗 Connect the model
)

# groq_agent = Agent(
#     name=f"🤖 Nawaz Lal ",  # Model name visible in agent's identity
#     instructions="You are a helpful assistant.",
#     # model=GROQ_MODEL
# )

groq_agent = Agent(
    name=f"🤖 Nawaz Lal",  # Model name visible in agent's identity
    instructions="You are a helpful assistant.",
    model="gemini-2.5-flash",                                                                                                                                                                                                                                                                                   
)
