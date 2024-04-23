# echo.py (in commands directory)
def register_command(subparser):
    """
    Register the 'echo' command.
    """
    subparser.add_argument("text", help="Text to echo")

def execute_command(args):
    """
    Execute the 'echo' command.
    """
    print(f"Echoing: {args.text}")
