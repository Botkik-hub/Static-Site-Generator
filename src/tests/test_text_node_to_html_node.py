from text_functions.text_node_to_html_node import *
import unittest

class TestTextToHtml(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")\
        
    def test_bold(self):
        node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold Text")
        
    def test_italic(self):
        node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic Text")
        
    def test_code(self):
        node = TextNode("Code Text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code Text")
        
    def test_link(self):
        node = TextNode("Link Text", TextType.TEXT_LINK, "test.url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link Text")
        self.assertEqual(html_node.props_to_html(), ' href="test.url"')
                
    def test_image(self):
        node = TextNode("Link Text", TextType.IMAGE_LINK, "test.url")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props_to_html(), ' src="test.url" alt="Link Text"')