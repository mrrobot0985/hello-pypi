# user_cli/actions/error_notifier.py
from .base_action import BaseAction

class ErrorNotifier(BaseAction):
    def trigger(self, message_type, message_content):
        return message_type == "error"

    def validate(self, context):
        return "CRITICAL" in message_content.upper()

    def execute(self, context):
        print("Critical error detected. Alerting admin.")
        # Perform additional logic, like sending an email or creating a log entry
