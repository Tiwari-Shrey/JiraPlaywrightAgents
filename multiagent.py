import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
async def main():
    model_client = OpenAIChatCompletionClient(model="gpt-4o")
    agent1 = AssistantAgent(name="MathTeacher",model_client=model_client, system_message="You are a math teacher. And explain concepts clearly and ask follow ups")
    agent2 = AssistantAgent(name="Student", model_client=model_client, system_message="You are a curious student and ask questions and show your thinking process")
    team = RoundRobinGroupChat(participants=[agent1,agent2],termination_condition=MaxMessageTermination(max_messages=6))

    await Console(team.run_stream(task="let's discuss what is multiplication and how it works"))
    await model_client.close()





asyncio.run(main())