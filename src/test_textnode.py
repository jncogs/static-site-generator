import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        print("------TEST TEXTNODE------")
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("Blargh", TextType.CODE, "www.totallyarealwebsite.gov")

        print(f"Node 1: {node}")
        print(f"Node 2: {node2}")
        print(f"Node 3: {node3}")

        self.assertEqual(node, node2)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node3)

        print(f"Node 1 = Node 2? {node == node2}")
        print(f"Node 1 = Node 3? {node == node3}")


if __name__ == "__main__":
    unittest.main()