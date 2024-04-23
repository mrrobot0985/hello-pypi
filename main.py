import os
import argparse
from .utils import get_version  # Function to retrieve the version from the correct source

# Fetching the current user's name, defaulting to 'User' if not found
current_user = os.environ.get('USER', 'User')

def print_welcome_message():
    """
    Display a welcome message when no arguments are provided.
    """
    print(f"Hello {current_user}!")
    print("Available commands:")
    print("  --version  Show the version of the CLI client")

def create_argument_parser():
    """
    Create and return an argument parser for the CLI client.
    """
    parser = argparse.ArgumentParser(
        description="A simple command-line client",
        add_help=True  # Adds the default help argument (-h, --help)
    )
    
    # Adding the '--version' argument
    parser.add_argument(
        "--version",
        action="version",
        version=get_version(),
        help="Show the version of the CLI client"
    )

    return parser

def cli_client():
    """
    Command-line interface (CLI) client entry point.
    """
    parser = create_argument_parser()

    # Parse command-line arguments
    args = parser.parse_args()

    # If no arguments are provided, print the welcome message
    if not vars(args):  # vars(args) returns a dictionary of arguments
        print_welcome_message()

if __name__ == "__main__":
    cli_client()
