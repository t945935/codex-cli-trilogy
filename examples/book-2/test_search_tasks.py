import unittest

from search_tasks import search


class SearchTasksTests(unittest.TestCase):
    def test_search_is_case_insensitive_and_preserves_display_text(self):
        self.assertEqual(search("api"), ["Review API design", "Test api client"])
        self.assertEqual(search("API"), ["Review API design", "Test api client"])

    def test_empty_search_returns_no_results(self):
        self.assertEqual(search(""), [])


if __name__ == "__main__":
    unittest.main()
