import re

def extract_markdown_images(text):
    expression = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(expression, text)
    return matches

def extract_markdown_links(text):
    expression = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(expression, text)
    return matches