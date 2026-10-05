import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import todo


class TodoProjectReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.data = Path(self.tmp.name) / "todos.json"
        self.patch_data = patch.object(todo, "DATA", self.data)
        self.patch_data.start()
        self.addCleanup(self.patch_data.stop)

    def write_json(self, value):
        self.data.write_text(json.dumps(value) + "\n", encoding="utf-8")

    def test_legacy_array_migrates_to_stable_ids(self):
        self.write_json(["Read the guide", "Run tests"])
        state = todo.load_state()
        self.assertEqual(state["schema_version"], 2)
        self.assertEqual(state["tasks"], [
            {"id": 1, "text": "Read the guide", "completed": False},
            {"id": 2, "text": "Run tests", "completed": False},
        ])
        self.assertEqual(json.loads(self.data.read_text(encoding="utf-8")), ["Read the guide", "Run tests"])

    def test_add_preserves_existing_and_persists_versioned_schema(self):
        self.write_json(["Old task"])
        with patch("builtins.print"):
            self.assertEqual(todo.main(["add", "New task"]), 0)
        saved = json.loads(self.data.read_text(encoding="utf-8"))
        self.assertEqual(saved["schema_version"], 2)
        self.assertEqual(saved["tasks"], [
            {"id": 1, "text": "Old task", "completed": False},
            {"id": 2, "text": "New task", "completed": False},
        ])

    def test_blank_add_does_not_modify_source_bytes(self):
        self.write_json(["Keep me"])
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["add", "   "]), 2)
        self.assertEqual(self.data.read_bytes(), before)

    def test_done_changes_only_target_record(self):
        self.write_json(["First", "Second"])
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "2"]), 0)
        self.assertEqual(todo.load_state()["tasks"], [
            {"id": 1, "text": "First", "completed": False},
            {"id": 2, "text": "Second", "completed": True},
        ])

    def test_unknown_id_does_not_change_file(self):
        self.write_json(["Only task"])
        before = self.data.read_bytes()
        with patch("builtins.print"):
            status = todo.main(["done", "99"])
        self.assertEqual(status, 2)
        self.assertEqual(self.data.read_bytes(), before)

    def test_noninteger_id_is_rejected_without_write(self):
        self.write_json(["Only task"])
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "abc"]), 2)
        self.assertEqual(self.data.read_bytes(), before)

    def test_marking_completed_task_twice_is_idempotent(self):
        self.write_json(["Only task"])
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "1"]), 0)
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "1"]), 0)
        self.assertEqual(self.data.read_bytes(), before)

    def test_open_filter_hides_completed_items(self):
        self.write_json(["Open task", "Done task"])
        with patch("builtins.print"):
            todo.main(["done", "2"])
        with patch("builtins.print") as output:
            self.assertEqual(todo.main(["list", "--open"]), 0)
        self.assertEqual([call.args[0] for call in output.call_args_list], ["1. [ ] Open task"])

    def test_corrupt_json_is_not_overwritten(self):
        self.data.write_text("not-json\n", encoding="utf-8")
        before = self.data.read_bytes()
        with patch("builtins.print") as output:
            self.assertEqual(todo.main(["add", "New"]), 1)
        self.assertIn("Cannot read or save todo data", output.call_args.args[0])
        self.assertEqual(self.data.read_bytes(), before)

    def test_legacy_blank_record_is_rejected_and_preserved(self):
        self.write_json(["Valid", "   "])
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["add", "New"]), 1)
        self.assertEqual(self.data.read_bytes(), before)

    def test_unknown_schema_version_is_rejected_and_preserved(self):
        self.write_json({"schema_version": 999, "tasks": []})
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "1"]), 1)
        self.assertEqual(self.data.read_bytes(), before)

    def test_unrecognized_task_fields_are_rejected(self):
        self.write_json({"schema_version": 2, "tasks": [
            {"id": 1, "text": "A", "completed": False, "owner": "someone"}
        ]})
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "1"]), 1)
        self.assertEqual(self.data.read_bytes(), before)

    def test_duplicate_ids_are_rejected(self):
        self.write_json({"schema_version": 2, "tasks": [
            {"id": 1, "text": "A", "completed": False},
            {"id": 1, "text": "B", "completed": False},
        ]})
        before = self.data.read_bytes()
        with patch("builtins.print"):
            self.assertEqual(todo.main(["done", "1"]), 1)
        self.assertEqual(self.data.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
