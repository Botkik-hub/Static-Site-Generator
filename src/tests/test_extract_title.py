from file_manipulations.extract_title import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_extract(self):
        text = "# Hello"
        result = extract_title(text)
        self.assertEqual(result, "Hello")
    def test_extract_multiline(self):
        text = "\ntest\n\n\n# Hello\nasbsddsf\n# Another\n"
        result = extract_title(text)
        self.assertEqual(result, "Hello")
    def test_extract_strip(self):
        text = "\ntest\n\n\n# Hello     \nasbsddsf\n# Another\n"
        result = extract_title(text)
        self.assertEqual(result, "Hello")

    def test_extract_no_space(self):
        text = "#Hello"
        self.assertRaises(Exception, lambda : extract_title(text))
    def test_extract_h2(self):
        text = "## Hello"
        self.assertRaises(Exception, lambda : extract_title(text))