from text_functions.markdown_to_html_node import *
from file_manipulations.extract_title import *

import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown = ""
    with open(from_path, 'r', encoding='utf-8') as file:
        markdown = file.read()

    template = ""
    with open(template_path, 'r', encoding='utf-8') as file:
        template = file.read()
    
    html_node = markdown_to_html_node(markdown) 
    html_string = html_node.to_html()
    
    page_title = extract_title(markdown)
    full_page = template.replace("{{ Title }}", page_title).replace("{{ Content }}", html_string)

    directory = os.path.dirname(dest_path)
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(dest_path, "w") as file:
        file.write(full_page)
    