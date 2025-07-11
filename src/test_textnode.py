import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("***Test Equal***")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Blargh", TextType.CODE, "www.totallyarealwebsite.gov")

        '''print(f"Node 1: {node}")
        print(f"Node 2: {node2}")
        print(f"Node 3: {node3}")'''

        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)
    
    def test_repr(self):
        print("***Test Repr***")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Blargh", TextType.CODE, "www.totallyarealwebsite.gov")

        self.assertEqual(str(node), "TextNode(This is a text node, bold, None)")
        self.assertEqual(str(node2), "TextNode(This is a text node, bold, None)")
        self.assertEqual(str(node3), "TextNode(Blargh, code, www.totallyarealwebsite.gov)")


if __name__ == "__main__":
    print("------TEST TEXTNODE------")
    unittest.main()