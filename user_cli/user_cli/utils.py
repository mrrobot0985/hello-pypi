import os
import textwrap

def create_command_file(command_name, commands_dir):
    """
    Create a new command file in the specified directory with the given command name.

    Args:
        command_name (str): Name of the new command.
        commands_dir (str): Directory where the command files are stored.

    Returns:
        str: Path to the newly created command file.
    """
    # Ensure the commands directory exists
    os.makedirs(commands_dir, exist_ok=True)

    # Define the new command file path
    command_file_path = os.path.join(commands_dir, f"{command_name}.py")

    # Check if the command file already exists to avoid overwriting
    if os.path.exists(command_file_path):
        raise FileExistsError(f"The command '{command_name}' already exists at {command_file_path}.")

    # Create the boilerplate content for the command
    command_content = textwrap.dedent(f"""
    def add_subcommand(subparsers):
        \"\"\"
        Adds '{command_name}' subcommand to the given subparsers object.
        \"\"\"
        {command_name}_parser = subparsers.add_parser(
            "{command_name}", help="{command_name} command"
        )

        # Example argument; you can add more arguments here
        {command_name}_parser.add_argument(
            "--example",
            type=str,
            help="Example argument for the {command_name} command"
        )
    """)

    # Write the command content to the new file
    with open(command_file_path, "w") as command_file:
        command_file.write(command_content)

    return command_file_path
