import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import MultiModalMessage
from autogen_agentchat.ui import Console
from autogen_core import Image
from autogen_ext.models.openai import OpenAIChatCompletionClient
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant = AssistantAgent(name="MultiModelAssistant", model_client=model_client)
    image = Image.from_file(Path(r"C:\Users\shrey.tiwari\Downloads\logo.jpg"))
    multimodel_message = MultiModalMessage(content=["What do you see in the image",image], source="user")
    await Console(assistant.run_stream(task=multimodel_message))
    await model_client.close()

asyncio.run(main())