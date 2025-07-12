import unittest

from textnode import TextNode, TextType
from nodefunctions import text_node_to_html_node, text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_text_node(self):
        print("***Test Text to Text Node***")
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        #print(output)
        self.assertListEqual(new_nodes, 
                             [
                                 TextNode("This is ", TextType.TEXT),
                                 TextNode("text", TextType.BOLD),
                                 TextNode(" with an ", TextType.TEXT),
                                 TextNode("italic", TextType.ITALIC),
                                 TextNode(" word and a ", TextType.TEXT),
                                 TextNode("code block", TextType.CODE),
                                 TextNode(" and an ", TextType.TEXT),
                                 TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                                 TextNode(" and a ", TextType.TEXT),
                                 TextNode("link", TextType.LINK, "https://boot.dev"),
                             ]
        )
        output = []
        for n in new_nodes:
            html_node = text_node_to_html_node(n)
            output.append(html_node.to_html())
        #print("".join(output))
        self.assertEqual("".join(output), 'This is <b>text</b> with an <i>italic</i> word and a <code>code block</code> and an <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan image" /> and a <a href="https://boot.dev">link</a>')

if __name__ == "__main__":
    print("------TEST TEXT TO TEXT NODE------")
    unittest.main()