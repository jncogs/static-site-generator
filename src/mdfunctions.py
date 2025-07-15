from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    stripped_blocks = []
    for b in blocks:
        stripped_blocks.append(b.strip())
    while "" in stripped_blocks:
        stripped_blocks.remove("")

    return stripped_blocks

def block_to_block_type(block):
    if re.findall(r"^\#{1,6} (.*)", block):
        return BlockType.HEADING
    if re.findall(r"^`{3}(.*)`{3}$", block, re.S):
        return BlockType.CODE
    
    test = True
    split_block = block.split("\n")
    for split in split_block:
        if not re.findall(r"^\>(.*)", split):
            test = False
    if test:
        return BlockType.QUOTE

    test = True
    for split in split_block:
        if not re.findall(r"^- (.*)", split):
            test = False
    if test:
        return BlockType.UNORDERED_LIST
    
    test = True
    i = 0
    for split in split_block:
        i += 1
        if not re.findall(rf"^[{i}]. (.*)", split):
            test = False
    if test:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

def extract_title(markdown):
    title = None
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == BlockType.HEADING:
            title = re.findall(r"^\#{1} (.*)", block)
        if title:
            break
    
    if title:
        return clean_md(title[0])
    raise Exception("No title header in markdown")

def clean_md(text):
    cleaned_text = text.replace("**", "")
    cleaned_text = cleaned_text.replace("_", "")
    cleaned_text = cleaned_text.replace("`", "")

    return cleaned_text