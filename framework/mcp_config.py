from autogen_ext.tools.mcp import StdioServerParams, McpWorkbench


class McpConfig:
    @staticmethod
    def get_mcp_workbench():
        playwright_server_params = StdioServerParams(command=r"C:\Program Files\nodejs\npx.cmd", args= ["-y", "@executeautomation/playwright-mcp-server"], read_timeout_seconds=60)
        return McpWorkbench(playwright_server_params)
