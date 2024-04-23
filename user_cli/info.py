import subprocess
import os
import platform
import json
import logging
from functools import lru_cache


class ModuleMetadata:
    """
    A class to retrieve various metadata, including Git-related information.
    """

    def __init__(self):
        self.module_name = self.get_module_name()
        self.module_version = self.get_latest_git_tag()
        self.cli_command = f'{self.get_username()}'
        self.os = self.get_os_type()
        self.username = self.get_username()
        self.hostname = self.get_hostname()
        self.git_metadata = self.get_git_metadata()
        self.json = self.display_metadata_as_json()

    @staticmethod
    def _check_for_fatal(output):
        """
        Check if the output contains the word 'fatal'.

        Returns:
            bool: True if 'fatal' is found in the output, otherwise False.
        """
        return "fatal" in output.lower()

    @staticmethod
    def _run_command(command):
        try:
            # Execute the command and capture output
            output = subprocess.check_output(
                command, stderr=subprocess.STDOUT, universal_newlines=True
            ).strip()

            # If output contains "fatal", return a warning and a default value
            if "fatal" in output.lower():
                logging.warning(f"Command '{command}' failed with a fatal error: {output}")
                return "N/A"

            return output
        except subprocess.CalledProcessError as e:
            # Handle errors when the command fails, logging the issue
            logging.error(f"Command '{command}' failed with error: {e.output.strip()}")
            return "N/A"  # Returning None to indicate failure

    @lru_cache(None)
    def get_os_type(self):
        """
        Get the type of the operating system.

        Returns:
            str: 'Windows' or 'Unix-like'.
        """
        return "Windows" if platform.system() == "Windows" else "Unix-like"

    @staticmethod
    def get_module_name():
        """
        Return the module name based on the current directory's basename.

        Returns:
            str: The name of the module or 'Unknown' if extraction fails.
        """
        try:
            current_file_path = os.path.abspath(__file__)
            parent_directory = os.path.dirname(current_file_path)
            module_name = os.path.basename(parent_directory)
            return module_name
        except Exception as e:
            logging.error(f"Error in getting module name: {e}")
            return "Unknown"
        
    @lru_cache(None)
    def get_username(self):
        """
        Get the current user's username.

        Returns:
            str: The username of the current user.
        """
        return self._run_command(["whoami"]) or "Unknown"

    @lru_cache(None)
    def get_hostname(self):
        """
        Get the hostname of the system.

        Returns:
            str: The hostname of the system.
        """
        return self._run_command(["hostname"]) or "Unknown"

    @lru_cache(None)
    @staticmethod
    def get_latest_git_tag(self):
        # Command to get the latest tag
        command = ["git", "tag", "--sort=-v:refname"]
        
        try:
            # Execute the command and capture the output
            output = subprocess.check_output(command, universal_newlines=True).splitlines()
            
            # The first line is the most recent tag
            latest_tag = output[0] if output else '0'
            
            return latest_tag
        
        except subprocess.CalledProcessError as e:
            print(f"Error retrieving Git tags: {e}")
            return "N/A"
        
    @lru_cache(None)
    def get_git_metadata(self):
        """
        Get Git metadata, including tag, author, email, branch, commit hash, commit message, and commit date.
        """
        git_data = {
            "git_tag": self.get_latest_git_tag() or "N/A",
            "git_username": self._run_command(["git", "config", "user.name"]) or "N/A",
            "git_email": self._run_command(["git", "config", "user.email"]) or "N/A",
            "git_branch": self._run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"]) or "N/A",
            "git_commit_hash": self._run_command(["git", "rev-parse", "--short", "HEAD"]) or "N/A",
            "git_commit_message": self._run_command(["git", "log", "-1", "--pretty=%B"]) or "N/A",
            "git_commit_date": self._run_command(["git", "log", "-1", "--pretty=%cd", "--date=format:'%Y-%m-%d %H:%M:%S'"]) or "N/A",
        }
        return git_data

    def display_metadata_as_json(self):
        """
        Display the metadata in a JSON format.
        """
        metadata = {
            "name": self.module_name,
            "os": self.os,
            "username": self.username,
            "hostname": self.hostname,
            "git_metadata": self.git_metadata,
        }

        json_output = json.dumps(metadata, indent=4)
        return json_output
