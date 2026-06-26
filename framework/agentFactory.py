from autogen_agentchat.agents import AssistantAgent

from framework.mcp_config import McpConfig


class AgentFactory:
    def __init__(self, model_client):
        self.model_client = model_client
        self.mcp_config = McpConfig()

    def create_playwright_agent(self, system_message):
        automation_agent = AssistantAgent(name="AutomationAgent", model_client=self.model_client, workbench=self.mcp_config.get_mcp_workbench(), system_message=system_message)
        return automation_agent