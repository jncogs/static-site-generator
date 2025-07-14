import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        print("***Test to HTML***")
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    '''def test_no_value_error(self):
        print("***Test no value error***")
        node = LeafNode("p", None)
        with self.assertRaises(ValueError) as cm:
            node.to_html()
        self.assertEqual(str(cm.exception), "LeafNode contains no value")'''

if __name__ == "__main__":
    print("------TEST LEAFNODE------")
    unittest.main()