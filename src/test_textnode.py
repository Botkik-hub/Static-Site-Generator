import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_no_url(self):
        node = TextNode("This is a text node", TextType.TEXT_LINK, "url1")
        node2 = TextNode("This is a text node", TextType.IMAGE_LINK, "url1")
        self.assertNotEqual(node, node2)
    def test_url(self):
        node = TextNode("This is a text node", TextType.IMAGE_LINK, "url1")
        node2 = TextNode("This is a text node", TextType.IMAGE_LINK, "url1")
        self.assertEqual(node, node2)
    def test_equal(self):
        node = TextNode(None, TextType.CODE)
        node2 = TextNode(None, TextType.CODE)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()