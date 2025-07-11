import unittest

from textnode import TextNode, TextType
from leafnode import LeafNode
from main import text_node_to_html_node

class TestText2HTML(unittest.TestCase):
    def test_text(self):
        print("----TEST TEXT TO HTML-----")
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        print(html_node)

        node2 = TextNode("Image Alt Text", TextType.IMAGE, "https://www.riskyclick.org")
        html_node2 = text_node_to_html_node(node2)
        print(html_node2)

if __name__ == "__main__":
    unittest.main()