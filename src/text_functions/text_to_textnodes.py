from markdown_nodes.textnode import *
from text_functions.split_nodes_image import *
from text_functions.split_nodes_link import * 
from text_functions.split_nodes_delimiter import *

def text_to_textnodes(str):
    if str is None or len(str) == 0:
        return []
    
    initial_node = TextNode(str, TextType.TEXT)
    result = split_nodes_delimiter([initial_node], "**", TextType.BOLD)
    result = split_nodes_delimiter(result, "_", TextType.ITALIC)
    result = split_nodes_delimiter(result, "`", TextType.CODE)
    result = split_nodes_image(result)
    result = split_nodes_link(result)
    return result
