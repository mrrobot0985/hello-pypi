# user_cli/context.py
class Context:
    def __init__(self):
        self.data = {}  # Dictionary to store various contextual information

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
