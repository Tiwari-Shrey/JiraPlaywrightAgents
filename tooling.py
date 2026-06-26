import asyncio
import os
from dotenv import load_dotenv
from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.tools.mcp import McpWorkbench, StdioServerParams
load_dotenv()
from mcp import StdioServerParameters

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    path = r"C:\Users\shrey.tiwari\agenticai"
    filesystem_server_params = StdioServerParams(command="npx", args = [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        path
    ],
    read_timeout_seconds = 60)
    fs_workbench = McpWorkbench(filesystem_server_params)
    async with fs_workbench as fs_wb:
        systemMessage=("You are a math teacher. Explain concepts clearly and ask follow ups. "
        "You have access to a filesystem. "
        "CRITICAL RULES FOR FILES:\n"
        "- You MUST ONLY use relative paths.\n"
        "- NEVER use paths starting with / or C:\\\n"
        "- All files must be inside the working directory.\n"
        "- Always save files like: 'topicname.txt'\n"
        "- If file doesn't exist, create it first.\n"
        "When user says THANKYOU, respond with LESSONCOMPLETED.")
        model_client = OpenAIChatCompletionClient(model="gpt-4o")
        assistant = AssistantAgent(name="MathTeacher", model_client=model_client,workbench = fs_wb , system_message=systemMessage)
        user_proxy = UserProxyAgent(name="Student")
        team = RoundRobinGroupChat(participants=[user_proxy, assistant], termination_condition=TextMentionTermination("LESSONCOMPLETED"))
        await Console(team.run_stream(task="I need help with algebra problem""feel free to create files for help in student learning"))
        await model_client.close()


asyncio.run(main())