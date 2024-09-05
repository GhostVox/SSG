import unittest

from copy_static import extract_title

class TestGenerateFuncs(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello world"
        self.assertEqual("Hello world", extract_title(markdown))

    def test_extract_title_no_H1(self):
        markdown = "## their is no h1 in this md."
        with self.assertRaises(Exception):
            extract_title(markdown)
    