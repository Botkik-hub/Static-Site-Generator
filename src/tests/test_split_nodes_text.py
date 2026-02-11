import unittest
from text_functions.split_nodes_link import *

class TestSplitDelimiterLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.TEXT_LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.TEXT_LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )
    def test_split_links_startwith(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png) and another [second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("image", TextType.TEXT_LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.TEXT_LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )
    def test_split_links_two_in_a_row(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)[second image](https://i.imgur.com/3elNhQu.png) and another ",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("image", TextType.TEXT_LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "second image", TextType.TEXT_LINK, "https://i.imgur.com/3elNhQu.png"
                ),
                TextNode(" and another ", TextType.TEXT),
            ]
        )
    def test_split_links_link_and_img(self):
        node = TextNode(
            "[image](https://i.imgur.com/zjjcJKZ.png)![second image](https://i.imgur.com/3elNhQu.png) and another ",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])

        self.assertEqual(
            new_nodes,
            [
                TextNode("image", TextType.TEXT_LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(
                    "![second image](https://i.imgur.com/3elNhQu.png) and another ", TextType.TEXT,
                ),
            ]
        )