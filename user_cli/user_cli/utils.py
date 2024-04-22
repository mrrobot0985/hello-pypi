import os

def get_version():
    # Read the version from `version.txt`
    config_dir = os.path.join(os.path.dirname(__file__), "config")
    version_file_path = os.path.join(config_dir, "version.txt")
    with open(version_file_path, "r") as f:
        return f.readline().strip()
