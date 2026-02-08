from markdown_nodes.textnode import *
from html_nodes.leafnode import *


def text_node_to_html_node(text_node):
    match text_node.type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.TEXT_LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE_LINK:
            return LeafNode("img", '', {"src" : text_node.url, "alt": text_node.text})
        case _:
            raise Exception(f"Unknown node type: {text_node.type.value}")
         