import importlib
import os
from .dynamic_parser_creator import DynamicParserCreator
from .message_handler import MessageHandler

def cli_client():
    command_dir = os.path.join(os.path.dirname(__file__), "commands")
    parser_creator = DynamicParserCreator(command_dir)
    parser = parser_creator.create_parser()

    args = parser.parse_args()

    action_dir=os.path.join(os.path.dirname(__file__), "actions")
    message_handler = MessageHandler(action_dir)

    if args.command:
        command_module = importlib.import_module(f"user_cli.commands.{args.command}")
        try:
            command_module.execute_command(args)  # Execute the specific command
            message_handler.send_message("info", f"Command '{args.command}' executed successfully.")
        except Exception as e:
            message_handler.send_message("error", f"Error executing command '{args.command}': {e}")
    else:
        parser.print_help()  # If no command, display help
