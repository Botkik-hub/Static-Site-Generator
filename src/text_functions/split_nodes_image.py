from text_functions.extract_refs import *
from markdown_nodes.textnode import *
def split_nodes_image(old_nodes):
    result_nodes = []

    for node in old_nodes:
        links = extract_markdown_images(node.text)
        if len(links) == 0:
            result_nodes.append(node)
            continue
        
        text_left = node.text
        for link in links:
            link_text = f"![{link[0]}]({link[1]})"
            if text_left.startswith(link_text):
                result_nodes.append(TextNode(link[0], TextType.IMAGE_LINK, link[1]))
                text_left = text_left.replace(link_text, "", 1)
            else:
                split = text_left.split(link_text, 1)
                result_nodes.append(TextNode(split[0], TextType.TEXT))
                result_nodes.append(TextNode(link[0], TextType.IMAGE_LINK, link[1]))
                if len(split) != 1:
                    text_left = split[1]
                else:
                    text_left = ''
        if text_left != '':
            result_nodes.append(TextNode(text_left, TextType.TEXT))        
        return result_nodes