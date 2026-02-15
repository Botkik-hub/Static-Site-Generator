from markdown_nodes.blocktype import *
import re


def block_to_block_type(block):
    if block is None or block == "":
        raise Exception("Block is none or empty string")
    if block.startswith("#") and not block.startswith("#######"): 
        no_hashes = block.replace("#", "")
        if no_hashes.startswith(" "):
            return BlockType.HEADING    
    if block.startswith("```\n") and block.endswith("```"):
        return BlockType.CODE
    
    lines = block.split("\n")
    all_quote = True
    all_unorderd = True
    all_ordered = True
    num_to_check = 1
    for line in lines:
        if all_quote:
            all_quote = line.startswith(">")
        if all_unorderd:
            all_unorderd = line.startswith("- ")
        if all_ordered:
            all_ordered = line.startswith(f"{num_to_check}. ")
            num_to_check += 1

        if not all_ordered and not all_unorderd and not all_quote:
            break
    
    if all_ordered:
        return BlockType.ORDERED_LIST
    if all_unorderd:
        return BlockType.UNORDERED_LIST
    if all_quote:
        return BlockType.QUOTE

    return BlockType.PARAGRAPH
