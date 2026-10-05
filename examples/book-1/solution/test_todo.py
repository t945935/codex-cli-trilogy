import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import todo


class TodoSolutionTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.data = Path(self.tempdir.name) / "todos.json"
        self.data.write_text("[]\n", encoding="utf-8")
        self.data_patch = patch.object(todo, "DATA", self.data)
        self.data_patch.start()
        self.addCleanup(self.data_patch.stop)

    def test_add_keeps_existing_tasks_and_list_shows_both(self):
        self.assertEqual(todo.main(["add", "First task"]), 0)
        self.assertEqual(todo.main(["add", "Second task"]), 0)
        self.assertEqual(json.loads(self.data.read_text(encoding="utf-8")), ["First task", "Second task"])
        with patch("builtins.print") as output:
            self.assertEqual(todo.main(["list"]), 0)
        self.assertEqual([call.args[0] for call in output.call_args_list], ["1. First task", "2. Second task"])

    def test_blank_task_does_not_change_file(self):
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["add", "   "]), 2)
        self.assertEqual(self.data.read_bytes(), before)

    def test_corrupt_json_is_reported_without_overwriting(self):
        self.data.write_text("not-json\n", encoding="utf-8")
        before = self.data.read_bytes()
        with patch("builtins.print") as output:
            self.assertEqual(todo.main(["add", "Another"]), 1)
        self.assertIn("Cannot read or save todo data:", output.call_args.args[0])
        self.assertEqual(self.data.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
