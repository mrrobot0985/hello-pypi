# messaging.py
import importlib
import os

# user_cli/messaging.py
from .action_manager import ActionManager

class MessageHandler:
    def __init__(self, action_dir):
        self.handlers = {
            "info": self.handle_info,
            "warning": self.handle_warning,
            "error": self.handle_error
        }
        self.action_manager = ActionManager(action_dir)  # Initialize with the action directory

    def send_message(self, message_type, message_content):
        handler = self.handlers.get(message_type)
        if handler:
            handler(message_content)
            self.action_manager.process_message(message_type, message_content)  # Process message to trigger actions
        else:
            print(f"No handler found for message type: {message_type}. Content: {message_content}")

    def handle_info(self, message):
        print(f"Info: {message}")

    def handle_warning(self, message):
        print(f"Warning: {message}")

    def handle_error(self, message):
        print(f"Error: {message}")
