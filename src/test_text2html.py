import unittest

from textnode import TextNode, TextType
from main import text_node_to_html_node

class TestText2HTML(unittest.TestCase):
    def test_text(self):
        print("***Test TEXT***")
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), "This is a text node")
    
    def test_bold(self):
        print("***Test BOLD***")
        node = TextNode("Bold this text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), "<b>Bold this text</b>")
    
    def test_italic(self):
        print("***Test ITALIC***")
        node = TextNode("Italic this text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), "<i>Italic this text</i>")
    
    def test_code(self):
        print("***Test CODE***")
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), "<code>This is code</code>")
    
    def test_link(self):
        print("***Test LINK***")
        node = TextNode("This is the link", TextType.LINK, "https://www.riskyclick.org")
        html_node = text_node_to_html_node(node)
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), '<a href="https://www.riskyclick.org">This is the link</a>')

    def test_image(self):
        print("***Test IMAGE***")
        node = TextNode("Image Alt Text", TextType.IMAGE, "https://www.riskyclick.org")
        html_node = text_node_to_html_node(node)
        #print(html_node)
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), '<img src="https://www.riskyclick.org" alt="Image Alt Text" />')
    
    def test_unknown_type(self):
        print("***Test Unknown Type***")
        node = TextNode("This will not be a real type", "JNCType")
        with self.assertRaises(Exception) as cm:
            html_node = text_node_to_html_node(node)
        self.assertEqual(str(cm.exception), "Unknown Text Type")

if __name__ == "__main__":
    print("----TEST TEXT TO HTML-----")
    unittest.main()