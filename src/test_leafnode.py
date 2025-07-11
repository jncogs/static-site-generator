import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_convert(self):
        print("-----TEST LEAF NODE------")
        node = LeafNode("p", "Hello, world!")
        print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

if __name__ == "__main__":
    unittest.main()