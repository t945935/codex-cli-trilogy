"""Executable acceptance tests for the book-2 todo feature.

Run with: python3 -m unittest -v feature_contract
These tests are deliberately outside the test_*.py discovery pattern so the
starter baseline suite remains green before the feature exercise.
"""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import todo


class TestTodoFeatureContract(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.data = Path(self.tmp.name) / "todos.json"
        self.data.write_text('["First", "Second"]\n', encoding="utf-8")
        self.data_patch = patch.object(todo, "DATA", self.data)
        self.data_patch.start()
        self.addCleanup(self.data_patch.stop)

    def test_done_migrates_and_changes_only_selected_task(self):
        with patch("builtins.print"):
            status = todo.main(["done", "2"])
        self.assertEqual(status, 0)
        saved = json.loads(self.data.read_text(encoding="utf-8"))
        self.assertEqual(saved, {"schema_version": 2, "tasks": [
            {"id": 1, "text": "First", "completed": False},
            {"id": 2, "text": "Second", "completed": True},
        ]})

    def test_unknown_id_is_rejected_without_changing_bytes(self):
        before = self.data.read_bytes()
        with patch("builtins.print") as output:
            status = todo.main(["done", "99"])
        self.assertEqual(status, 2)
        self.assertIn("not found", output.call_args.args[0])
        self.assertEqual(self.data.read_bytes(), before)

    def test_noninteger_id_is_rejected_without_changing_bytes(self):
        before = self.data.read_bytes()
        with patch("builtins.print") as output:
            status = todo.main(["done", "abc"])
        self.assertEqual(status, 2)
        self.assertIn("integer", output.call_args.args[0])
        self.assertEqual(self.data.read_bytes(), before)

    def test_repeating_done_does_not_toggle_state(self):
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "2"]), 0)
        before = self.data.read_bytes()
        with patch("builtins.print") as output:
            self.assertEqual(todo.main(["done", "2"]), 0)
        self.assertIn("already complete", output.call_args.args[0])
        self.assertEqual(self.data.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
