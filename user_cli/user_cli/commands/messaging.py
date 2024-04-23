# user_cli/commands/messaging.py
def register_command(subparser):
    subparser.add_argument("message", type=str, help="The message to send")
    subparser.add_argument("--level", choices=["info", "warning", "error"], default="info", help="Message level")

def execute_command(args):
    from ..messaging import MessageHandler
    message_handler = MessageHandler()
    message_handler.send_message(args.level, args.message)
