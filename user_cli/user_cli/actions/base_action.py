# user_cli/actions/base_action.py
class BaseAction:
    def trigger(self, message_type, message_content):
        raise NotImplementedError("Subclasses must implement 'trigger' method")

    def validate(self, context):
        raise NotImplementedError("Subclasses must implement 'validate' method")

    def execute(self, context):
        raise NotImplementedError("Subclasses must implement 'execute' method")
