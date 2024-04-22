from setuptools import setup, find_packages
import os
from info import ModuleMetadata

module = ModuleMetadata()

module_name = module.module_name
module_version = module.module_version
cli_command = module.cli_command

# # Ensure the config directory exists
config_dir = f"{module_name}/config"
os.makedirs(config_dir, exist_ok=True)

# Write the version to `version.txt`
with open(os.path.join(config_dir, "version.txt"), "w") as f:
    f.write(module_version)

setup(
    name=module_name,
    version=module_version,
    packages=find_packages(),
    install_requires=[],
    package_data={f"{module_name}": ["config/version.txt"]},  # Include version.txt in the package
    entry_points={
        "console_scripts": [
            f"{cli_command} = {module_name}:cli_client",
            ],
        },
)