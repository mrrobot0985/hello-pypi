import importlib
import os
from .context import Context
from .actions.base_action import BaseAction

class ActionManager:
    def __init__(self, action_dir):
        self.actions = self.load_actions(action_dir)
        self.context = Context()  # Initialize context

    def load_actions(self, action_dir):
        action_modules = [
            filename[:-3] for filename in os.listdir(action_dir) 
            if filename.endswith(".py") and not filename.startswith("__")
        ]
        
        actions = []
        for module_name in action_modules:
            module = importlib.import_module(f"user_cli.actions.{module_name}")
            for name, obj in module.__dict__.items():
                if isinstance(obj, type) and issubclass(obj, BaseAction) and obj is not BaseAction:
                    actions.append(obj())
        
        return actions
    
    def process_message(self, message_type, message_content):
        for action in self.actions:
            if action.trigger(message_type, message_content) and action.validate(self.context):
                action.execute(self.context)
