import os
import importlib
from argparse import ArgumentParser

class DynamicParserCreator:
    def __init__(self, command_dir):
        self.command_dir = command_dir

    def create_parser(self):
        parser = ArgumentParser(
            description="A simple command-line client",
            add_help=True,
        )

        subparsers = parser.add_subparsers(dest="command", help="Available commands")

        command_modules = self._detect_command_modules()

        for module_name in command_modules:
            module = importlib.import_module(f"user_cli.commands.{module_name}")

            if hasattr(module, "register_command"):
                subparser = subparsers.add_parser(module_name, help=f"{module_name} command")
                module.register_command(subparser)

        return parser

    def _detect_command_modules(self):
        return [
            filename[:-3] for filename in os.listdir(self.command_dir)
            if filename.endswith(".py") and not filename.startswith("__")
        ]
