from markdown_nodes.textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.type != TextType.TEXT:
            result.append(node)
            continue
        if delimiter not in node.text:
            result.append(node)
            continue
        split = node.text.split(delimiter)
        if len(split) % 2 == 0:
            raise Exception(f"Invalid Markdown syntax: delimiter {delimiter} have no pair in {node.text}")
        is_inside = node.text.startswith(delimiter)
        if is_inside:
            del split[0]
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
    return result