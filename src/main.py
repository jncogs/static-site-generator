from textnode import TextNode, TextType
from leafnode import LeafNode
from link_leafnode import LinkLeafNode
from img_leafnode import ImgLeafNode

def main():
    tn = TextNode("This is some test text", TextType.LINK, "https://www.boot.dev")
    print(tn)

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

main()