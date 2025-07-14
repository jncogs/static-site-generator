import re
from textnode import TextType
from htmlnode import HTMLNode
from leafnode import LeafNode
from mdfunctions import BlockType, markdown_to_blocks, block_to_block_type
from nodefunctions import text_node_to_html_node, text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        match (block_type):
            case (BlockType.PARAGRAPH):
                html_node = HTMLNode("p", value=__paragraph_to_html(block))
                children.append(html_node)
            case (BlockType.HEADING):
                heading, level = __heading_to_html(block)
                html_node = HTMLNode(f"h{level}", value=heading)
                children.append(html_node)
            case (BlockType.CODE):
                html_node = HTMLNode("pre", children=[__code_block_to_html_node(block)])
                children.append(html_node)
            case (BlockType.QUOTE):
                html_node = HTMLNode("blockquote", value=__quote_to_html(block))
                children.append(html_node)
            case (BlockType.UNORDERED_LIST):
                html_node = HTMLNode("ul", children=__unordered_list_to_html_node(block))
                children.append(html_node)
            case (BlockType.ORDERED_LIST):
                html_node = HTMLNode("ol", children=__ordered_list_to_html_node(block))
                children.append(html_node)
            case _:
                raise Exception("Unknown block type")
    return HTMLNode("div", children=children)

def __paragraph_to_html(block):
    children = []
    nodes = text_to_textnodes(block)
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node.to_html())
    return "".join(children)

def __heading_to_html(block):
    children = []
    i = 0
    for char in block:
        if char == "#" and i <= 6:
            i += 1
        else:
            break
    matches = re.findall(r"^\#{1,6} (.*)", block)
    nodes = text_to_textnodes(matches[0])
    for node in nodes:
        html_node = text_node_to_html_node(node)
        children.extend(html_node.to_html())
    return "".join(children), i

def __code_block_to_html_node(block):
    matches = re.findall(r"^`{3}(.*)`{3}$", block, re.S)
    html_node = LeafNode("code", matches[0])
    return html_node

def __quote_to_html(block):
    quotes = []
    children = []
    split_block = block.split("\n")
    for split in split_block:
        matches = re.findall(r"^\>(.*)", split)

        nodes = text_to_textnodes("".join(matches[0]))
        for node in nodes:
            html_node = text_node_to_html_node(node)
            children.append(html_node.to_html())
            if split_block.index(split) < len(split_block) - 1:
                children.append("<br>")
    return "".join(children)

def __unordered_list_to_html_node(block):
    children = []
    split_block = block.split("\n")
    for split in split_block:
        sub_children = []
        matches = re.findall(r"^\- (.*)", split)
        nodes = text_to_textnodes(matches[0])
        for node in nodes:
            html_node = text_node_to_html_node(node)
            sub_children.append(html_node.to_html())
        html_node = HTMLNode("li", value="".join(sub_children))
        children.append(html_node)
    
    return children

def __ordered_list_to_html_node(block):
    children = []
    split_block = block.split("\n")
    for split in split_block:
        sub_children = []
        matches = re.findall(r"^\d*. (.*)", split)
        nodes = text_to_textnodes(matches[0])
        for node in nodes:
            html_node = text_node_to_html_node(node)
            sub_children.append(html_node.to_html())
        html_node = HTMLNode("li", value="".join(sub_children))
        children.append(html_node)
    return children