import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant = AssistantAgent(name="assistant",model_client=model_client)
    await Console(assistant.run_stream(task="What is 25*6"))
    await model_client.close()

asyncio.run(main())