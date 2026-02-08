from textnode import *
from htmlnode import *

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
            

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            result.append(node)
            continue
        if delimiter not in node.text:
            result.append(node)
        split = node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: delimiter {delimiter} have no pair in {node.text}")
        is_inside = node.text.startswith(delimiter)
        i = 0
        while i < len(split):
            if is_inside:
                type = text_type
            else:
                type = TextType.TEXT
            new_node = TextNode(type=type, text=split[i])
            is_inside = not is_inside
            i += 1
            result.append(new_node)
    print(f"Function done, result length: {len(result)}")
    return result
            
            