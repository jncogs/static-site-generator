import re

from textnode import TextNode, TextType
from leafnode import LeafNode
from link_leafnode import LinkLeafNode
from img_leafnode import ImgLeafNode

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case (TextType.TEXT):
            return LeafNode(None, text_node.text)
        case (TextType.BOLD):
            return LeafNode("b", text_node.text)
        case (TextType.ITALIC):
            return LeafNode("i", text_node.text)
        case (TextType.CODE):
            return LeafNode("code", text_node.text)
        case (TextType.LINK):
            return LinkLeafNode("a", text_node.text, props={"href": text_node.url})
        case (TextType.IMAGE):
            return ImgLeafNode("img", props={"src": text_node.url,
                                              "alt": text_node.text})
        case __:
            raise Exception("Unknown Text Type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    if (delimiter != "**" and
        delimiter != "_" and
        delimiter != "`"):
            raise Exception("Given delimiter does not follow Markdown syntax")

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            current_type = TextType.TEXT
            subnodes = node.text.split(delimiter)
            for subnode in subnodes:
                new_node = TextNode(subnode, current_type)
                new_nodes.append(new_node)
                if current_type == TextType.TEXT:
                    current_type = text_type
                else:
                    current_type = TextType.TEXT
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if not images and node:
                new_nodes.append(node)
            elif images:
                text = node.text
                for image in images:
                    image_alt, image_url = image
                    sections = text.split(f"![{image_alt}]({image_url})", 1)
                    text = sections[1]
                    new_nodes.extend([TextNode(sections[0], TextType.TEXT), TextNode(image_alt, TextType.IMAGE, image_url)])
                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if not links and node:
                new_nodes.append(node)
            elif links:
                text = node.text
                for link in links:
                    link_anchor, link_url = link
                    sections = text.split(f"[{link_anchor}]({link_url})", 1)
                    text = sections[1]
                    new_nodes.extend([TextNode(sections[0], TextType.TEXT), TextNode(link_anchor, TextType.LINK, link_url)])
                if text:
                    new_nodes.append(TextNode(text, TextType.TEXT))
    
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    output = split_nodes_delimiter([node], "**", TextType.BOLD)
    output = split_nodes_delimiter(output, "_", TextType.ITALIC)
    output = split_nodes_delimiter(output, "`", TextType.CODE)
    output = split_nodes_image(output)
    output = split_nodes_links(output)

    return output