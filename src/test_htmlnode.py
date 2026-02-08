from htmlnode import *
import unittest

class TestHTMLNode(unittest.TestCase):
    def test_equal_1_prop(self):
        node = HTMLNode(None, None, None, {"test":"123"})        
        result = node.props_to_html()
        expected = ' test="123"'
        self.assertEqual(result, expected)
    def test_equal_2_prop(self):
        node = HTMLNode(None, None, None, {"test":"123", "test2":"4321"})        
        result = node.props_to_html()
        expected = ' test="123" test2="4321"'
        self.assertEqual(result, expected)
    def test_prop_to_html_none(self):
        node = HTMLNode(None, None, None, None)        
        result = node.props_to_html()
        expected = ''
        self.assertEqual(result, expected)
    def test_prop_to_html_empty(self):
        node = HTMLNode(None, None, None, {})        
        result = node.props_to_html()
        expected = ''
        self.assertEqual(result, expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), 'Click me!')
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_multiple_children(self):
        node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")