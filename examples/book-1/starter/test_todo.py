import unittest
from unittest.mock import patch

import todo


class TodoStarterTests(unittest.TestCase):
    def test_empty_list_prints_helpful_message(self):
        with patch.object(todo, "load_tasks", return_value=[]):
            with patch("builtins.print") as output:
                self.assertEqual(todo.main(["list"]), 0)
        output.assert_called_once_with("No tasks yet.")

    def test_unsupported_command_shows_usage(self):
        with patch("builtins.print") as output:
            self.assertEqual(todo.main(["add", "example"]), 2)
        output.assert_called_once_with("Usage: python3 todo.py list")


if __name__ == "__main__":
    unittest.main()
