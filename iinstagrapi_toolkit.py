from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
# from greetings_tool import GreetingsTool
from instagrapi_tool import InstagrapiTool



# class GreetingsToolkit(BaseToolkit, ABC):
#     name: str = "Greetings Toolkit"
#     description: str = "Greetings Tool kit contains all tools related to Greetings"

#     def get_tools(self) -> List[BaseTool]:
#         return [GreetingsTool()]

#     def get_env_keys(self) -> List[str]:
#         return ["FROM"]
    
    
class InstagrapiToolkit(BaseToolkit, ABC):
    name: str = "Instagrapi Toolkit"
    description: str = "Instagrapi Tool kit contains all tools related to Instagram"

    def get_tools(self) -> List[BaseTool]:
        return [InstagrapiTool()]

    def get_env_keys(self) -> List[str]:
        return ["FROM"]