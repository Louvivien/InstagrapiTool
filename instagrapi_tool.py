from superagi.tools.base_tool import BaseTool
from instagrapi import Client
from instagrapi.exceptions import ClientError
from instagrapi.exceptions import LoginRequired
from pydantic import BaseModel, Field
from typing import Type


class InstagrapiInput(BaseModel):
    message: str = Field(..., description="Message to be sent")


class InstagrapiTool(BaseTool):
    """
    Instagrapi Tool
    """
    name: str = "Instagrapi Tool"
    args_schema: Type[BaseModel] = InstagrapiInput
    description: str = "Tool for sending a message that you have previously written to a user on Instagram. Do not write the message you want to send in a file or it will not work."

    def _execute(self, message: str = None):
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
            message_str = "Message sent successfully"
            print(message_str )
            return  message_str 

        except ClientError as e:
            print('Message failed')
            print(e)
    
  