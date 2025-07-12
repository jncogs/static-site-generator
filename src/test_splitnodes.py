import unittest

from nodefunctions import text_node_to_html_node, split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodeDelim(unittest.TestCase):
    def test_other_types(self):
        print("***Test Split Non Text***")
        node = TextNode("This is `CODE` node", TextType.CODE)
        node2 = TextNode("This is an **IMAGE** node", TextType.IMAGE, "www.riskyclick.org")
        node3 = TextNode("This is a _LINK_ node", TextType.LINK, "www.testlink.com")

        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        #print(nodes[0])
        self.assertEqual(str(nodes[0]), "TextNode(This is `CODE` node, code, None)")
        html_node = text_node_to_html_node(nodes[0])
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), "<code>This is `CODE` node</code>")

        nodes = split_nodes_delimiter([node2], "**", TextType.BOLD)
        #print(nodes[0])
        self.assertEqual(str(nodes[0]), "TextNode(This is an **IMAGE** node, image, www.riskyclick.org)")
        html_node = text_node_to_html_node(nodes[0])
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), '<img src="www.riskyclick.org" alt="This is an **IMAGE** node" />')

        nodes = split_nodes_delimiter([node3], "_", TextType.ITALIC)
        #print(nodes[0])
        self.assertEqual(str(nodes[0]), "TextNode(This is a _LINK_ node, link, www.testlink.com)")
        html_node = text_node_to_html_node(nodes[0])
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), '<a href="www.testlink.com">This is a _LINK_ node</a>')

    def test_text(self):
        print("***Testing plain text containing no delimiters***")
        node = TextNode("This is my text.  No delimiters here!", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        #print(nodes[0])
        self.assertEqual(str(nodes[0]), "TextNode(This is my text.  No delimiters here!, text, None)")
        html_node = text_node_to_html_node(nodes[0])
        #print(html_node.to_html())
        self.assertEqual(html_node.to_html(), "This is my text.  No delimiters here!")

    def test_bold(self):
        print("***Test Bold Split***")
        node = TextNode("This text contains **some BOLD ideas**!!!", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        #print(str(nodes))
        self.assertEqual(str(nodes), "[TextNode(This text contains , text, None), TextNode(some BOLD ideas, bold, None), TextNode(!!!, text, None)]")
        html_nodes = []
        for n in nodes:
            html_node = text_node_to_html_node(n)
            html_nodes.append(html_node.to_html())
        #print("".join(html_nodes))
        self.assertEqual("".join(html_nodes), "This text contains <b>some BOLD ideas</b>!!!")
        
    def test_italic(self):
        print("***Test Italic Split***")
        node = TextNode("This text contains more _nuanced ideas_.", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        #print(str(nodes))
        self.assertEqual(str(nodes), "[TextNode(This text contains more , text, None), TextNode(nuanced ideas, italic, None), TextNode(., text, None)]")
        html_nodes = []
        for n in nodes:
            html_node = text_node_to_html_node(n)
            html_nodes.append(html_node.to_html())
        #print("".join(html_nodes))
        self.assertEqual("".join(html_nodes), "This text contains more <i>nuanced ideas</i>.")

    def test_code(self):
        print("***Test Code Split***")
        node = TextNode("This is an example of some Pascal code: `PROCEDURE: Blah blah blah;`. Oh my! How...inelegant!", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        #print(str(nodes))
        self.assertEqual(str(nodes), "[TextNode(This is an example of some Pascal code: , text, None), TextNode(PROCEDURE: Blah blah blah;, code, None), TextNode(. Oh my! How...inelegant!, text, None)]")
        html_nodes = []
        for n in nodes:
            html_node = text_node_to_html_node(n)
            html_nodes.append(html_node.to_html())
        #print("".join(html_nodes))
        self.assertEqual("".join(html_nodes), "This is an example of some Pascal code: <code>PROCEDURE: Blah blah blah;</code>. Oh my! How...inelegant!")

    def test_unknown_delim(self):
        print("***Test a bad delimiter***")
        node = TextNode("This one will use an incorrect <delimiter<", TextType.TEXT)
        with self.assertRaises(Exception) as cm:
            nodes = split_nodes_delimiter([node], "<", TextType.BOLD)
        #print(cm.exception)
        self.assertEqual(str(cm.exception), "Given delimiter does not follow Markdown syntax")
        

if __name__ == "__main__":
    print("------TEST SPLIT NODE DELIMITER------")
    unittest.main()