# main.py
import importlib
import os
import argparse

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="Dynamic CLI")
        self.subparsers = self.parser.add_subparsers(dest="command", help="Available commands")

        # Discover submodules in the 'commands' directory
        self.load_submodules()

    def load_submodules(self):
        # Dynamically import submodules from 'commands' directory
        command_dir = os.path.dirname(__file__) + "/commands"
        for file_name in os.listdir(command_dir):
            if file_name.endswith(".py") and not file_name.startswith("__"):
                module_name = "user_cli.commands." + file_name[:-3]
                module = importlib.import_module(module_name)
                
                # Check if the module has 'add_subcommand' function
                if hasattr(module, "add_subcommand"):
                    # Pass the subparser reference to the module's add_subcommand
                    module.add_subcommand(self.subparsers)

    def parse_arguments(self):
        return self.parser.parse_args()
