import unittest

from textnode import TextNode, TextType
from nodefunctions import text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_images(self):
        print("***Test Extract Markdown Image Regex***")
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        matches = extract_markdown_images(text)
        #print(matches)
        self.assertListEqual([('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')], matches)
    
    def test_extract_links(self):
        print("***Test Extract Markdown Links Regex***")
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        matches = extract_markdown_links(text)
        #print(matches)
        self.assertListEqual([('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')], matches)

    def test_split_nodes_image(self):
        print("***Test Split Node Image***")
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_image([node])
        #print(new_nodes)
        self.assertListEqual(new_nodes,
                            [
                                TextNode("This is text with a ", TextType.TEXT),
                                TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
                                TextNode(" and ", TextType.TEXT),
                                TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                            ]
        )
        output = []
        for n in new_nodes:
            html_node = text_node_to_html_node(n)
            output.append(html_node.to_html())
        #print("".join(output))
        self.assertEqual("".join(output), 'This is text with a <img src="https://i.imgur.com/aKaOqIh.gif" alt="rick roll" /> and <img src="https://i.imgur.com/fJRm4Vk.jpeg" alt="obi wan" />')
    
    def test_split_nodes_link(self):
        print("***Test Split Node Link***")
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        node = TextNode(text, TextType.TEXT)
        new_nodes = split_nodes_links([node])
        #print(new_nodes)
        self.assertListEqual(new_nodes, 
                             [
                                 TextNode("This is text with a link ", TextType.TEXT),
                                 TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                                 TextNode(" and ", TextType.TEXT),
                                 TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
                             ]
        )
        output = []
        for n in new_nodes:
            html_node = text_node_to_html_node(n)
            output.append(html_node.to_html())
        print("".join(output))
        self.assertEqual("".join(output), 'This is text with a link <a href="https://www.boot.dev">to boot dev</a> and <a href="https://www.youtube.com/@bootdotdev">to youtube</a>')

if __name__ == "__main__":
    print('-----TEST EXTRACT MARKDOWN------')
    unittest.main()