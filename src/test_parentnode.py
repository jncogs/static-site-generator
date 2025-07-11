import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        print("***Test To HTML w/ Children***")
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        #print(parent_node.to_html())

    def test_to_html_with_grandchildren(self):
        print("***Test To HTML w/ Grandchildren***")
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        #print(parent_node.to_html())
    
    def test_no_tag_given(self):
        print("***Test No Tag Given***")
        child_node = LeafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        #print(cm.exception)
        self.assertEqual(str(cm.exception), "No tag given")
    
    def test_no_children_given(self):
        print("***Test No Children Given***")
        parent_node = ParentNode("span", [])
        with self.assertRaises(ValueError) as cm:
            parent_node.to_html()
        #print(cm.exception)
        self.assertEqual(str(cm.exception), "No children")

if __name__ == "__main__":
    print("------TEST PARENTNODE------")
    unittest.main()