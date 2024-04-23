import unittest
from user_cli.action_manager import ActionManager
from user_cli.actions.error_notifier import ErrorNotifier  # Importing a custom action
from user_cli.actions.base_action import BaseAction

class TestActionManager(unittest.TestCase):
    def setUp(self):
        # Initialize ActionManager for each test
        self.action_manager = ActionManager()

    def test_register_action(self):
        # Ensure that actions can be registered
        action = ErrorNotifier()  # Example action
        self.action_manager.register_action(action)
        self.assertIn(action, self.action_manager.actions)  # Check if action is registered

    def test_trigger_action(self):
        # Ensure that actions are triggered correctly
        class MockAction(BaseAction):
            def __init__(self):
                super().__init__("mock_action")
                self.triggered = False

            def trigger(self, message):
                self.triggered = True  # Set a flag to indicate the trigger happened

        mock_action = MockAction()
        self.action_manager.register_action(mock_action)
        self.action_manager.trigger("mock_action", "Test Message")

        self.assertTrue(mock_action.triggered)  # Check if the action was triggered

    def test_invalid_trigger(self):
        # Test triggering a non-existing action
        with self.assertRaises(ValueError):  # Should raise an error for unknown triggers
            self.action_manager.trigger("non_existing_action", "Test Message")


if __name__ == "__main__":
    unittest.main()
