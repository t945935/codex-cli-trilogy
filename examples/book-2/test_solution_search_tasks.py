import unittest

from solution_search_tasks import search


class SearchSolutionTests(unittest.TestCase):
    def test_query_case_does_not_change_matches(self):
        expected = ["Review API design", "Test api client"]
        self.assertEqual(search("api"), expected)
        self.assertEqual(search("API"), expected)
        self.assertEqual(search("Api"), expected)

    def test_empty_query_and_no_match(self):
        self.assertEqual(search(""), [])
        self.assertEqual(search("missing"), [])


if __name__ == "__main__":
    unittest.main()
