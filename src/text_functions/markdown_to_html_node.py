from text_functions.markdown_to_blocks import *
from text_functions.block_to_block_type import *
from text_functions.text_to_textnodes import *
from text_functions.text_node_to_html_node import *

from html_nodes.parentnode import *

def get_heading_level(text):
    for i in range(6, 0, -1):
        str = "#" * i + " "
        if text.startswith(str):
            return i
     
    raise Exception(f"Could not handle Heading: {text}")

def handle_heading(text):
    nodes = text_to_textnodes(text)
    if nodes is None:
        raise Exception("nodes are None, something went wrong")
    first_node_text = nodes[0].text

    heading_level = get_heading_level(first_node_text)
    nodes[0].text = first_node_text.replace("#" * heading_level + " ", "")
    if nodes[0].text.strip() == "":
        del nodes[0]

    html_nodes = [text_node_to_html_node(node) for node in nodes]

    return ParentNode(f"h{heading_level}", html_nodes) 
    
def handle_code(text):
    text = text.replace("```\n", "", 1)
    text = text.removesuffix("```")
    return ParentNode("pre", [LeafNode("code", text)])

def handle_paragraph(text):
    nodes = text_to_textnodes(text.replace("\n", " "))
    html_nodes = [text_node_to_html_node(node) for node in nodes]
    return ParentNode("p", html_nodes) 

def handle_quote(text):
    new_text = ""
    for line in text.split("\n"):
        new_line = line.replace(">", "")
        if not new_line.startswith(" "):
            new_line = " " + new_line
        new_text += new_line
    new_text = new_text[1:] # remove first space
    nodes = text_to_textnodes(new_text)
    html_nodes = [text_node_to_html_node(node) for node in nodes]
    return ParentNode("blockquote", html_nodes) 

def handle_unordered_list(text):
    lines = text.split("\n")
    nodes = []
    for line in lines:
        line = line.replace("- ", "")
        html_nodes = [text_node_to_html_node(node) for node in text_to_textnodes(line)]
        nodes.append(ParentNode("li", html_nodes))
    return ParentNode("ul", nodes)


def handle_ordered_list(text):
    lines = text.split("\n")
    nodes = []
    last_index = 1
    for line in lines:
        line = line.replace(f"{last_index}. ", "")
        html_nodes = [text_node_to_html_node(node) for node in text_to_textnodes(line)]
        nodes.append(ParentNode("li", html_nodes))
        last_index += 1
    return ParentNode("ol", nodes)

def node_to_childrens(block):
    type = block_to_block_type(block)

    match type:
        case BlockType.PARAGRAPH:
            return handle_paragraph(block)
        case BlockType.HEADING:
            return handle_heading(block)
        case BlockType.CODE:
            return handle_code(block)
        case BlockType.QUOTE:
            return handle_quote(block)
        case BlockType.UNORDERED_LIST:
            return handle_unordered_list(block)
        case BlockType.ORDERED_LIST:
            return handle_ordered_list(block)
    raise Exception("Unkonwn block type")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []

    for block in blocks:
        nodes = node_to_childrens(block)
        html_nodes.append(nodes)

    return ParentNode("div", html_nodes)

