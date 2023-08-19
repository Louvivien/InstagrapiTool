from superagi.tools.base_tool import BaseTool
from instagrapi import Client
from instagrapi.exceptions import ClientError
from instagrapi.exceptions import LoginRequired
from pydantic import BaseModel, Field
from typing import Type


# class GreetingsInput(BaseModel):
#     greetings: str = Field(..., description="Greeting message to be sent")


class InstagrapiInput(BaseModel):
    message: str = Field(..., description="Message to be sent")


class InstagrapiTool(BaseTool):
    """
    Instagrapi Tool
    """
    # OK
    name: str = "Instagrapi Tool"
    # OK
    args_schema: Type[BaseModel] = InstagrapiInput
    # OK
    description: str = "Tool for sending a message that you have previously written to a user on Instagram. Do not write the message you want to send in a file or it will not work."

    # def _execute(self, message: str = None):
    #     from_name = self.get_tool_config('FROM')
    #     greetings_str = greetings + "\n" + from_name
    #     return greetings_str

    
    def send_message(self, message: str = None):
        # if isinstance(tool_input, str):
        #     tool_input = InstagramSendInputSchema(tool_input=tool_input)
        # message = tool_input.tool_input
        # print(f"Arguments: {tool_input}")

        # # Check if the message is empty
        # if not message:
        #     return "You did not write a message to send, in order to use this tool you need to write a message to the user, try again please"
        # print(f"Message: {message}")  # Log the message

        # # Check if the message is the same as the last sent message
        # if message == self.last_sent_message:
        #     print("Message is the same as the last sent message. Skipping sending. Did you wait for the user reply? Suggest using instagram_receive")
        #     return "Message is the same as the last sent message. Skipping sending. Did you wait for the user reply? Suggest using instagram_receive"

        try:
            result = self.client.direct_send(message, user_ids="louvivien")
            thread_id = result.thread_id
            thread = self.client.direct_thread(thread_id)
            # Store last_message_id, thread_id, last_sent_message, and last_sent_timestamp as instance variables
            self.last_message_id = thread.messages[0].id
            self.thread_id = result.thread_id
            self.last_sent_message = message
            self.last_sent_timestamp = thread.messages[0].timestamp
            print("Message sent successfully")
            return  "Message sent successfully"

        except ClientError as e:
            print('Message failed')
            print(e)
    
    
# class GreetingsTool(BaseTool):
#     """
#     Greetings Tool
#     """
#     name: str = "Greetings Tool"
#     args_schema: Type[BaseModel] = GreetingsInput
#     description: str = "Sends a Greeting Message"

#     def _execute(self, greetings: str = None):
#         from_name = self.get_tool_config('FROM')
#         greetings_str = greetings + "\n" + from_name
#         return greetings_str



# //////////////


# Validation rules for Auto-GPT
# class InstagramSendInputSchema(BaseModel):
#     tool_input: str = Field(...)

#     @root_validator
#     def validate_input(cls, values: Dict[str, Any]) -> Dict:
#         tool_input = values["tool_input"]
#         if not tool_input:
#             raise ValueError("You are using the send_message tool without providing a message to send. To make this work you first need to write the message then use this tool. Do not write the message in a file or it will not work")

#         if tool_input.endswith('.txt'):
#             raise ValueError("You are using the send_message tool with a file. This tool does not work with files, you need to write a regular message, not provide a file")

#         return values