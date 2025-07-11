import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        print("***Test Repr***")
        node = HTMLNode(tag="p", value="This is the value of the thing", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Value blah blah blah")
        child1 = HTMLNode(value="I'm a child!")
        child2 = HTMLNode(value="I'm also a child")
        node3 = HTMLNode(tag="h1", children=[child1, child2])

        self.assertEqual(str(node),
                         "Tag: p\n" \
                         "Value: This is the value of the thing\n" \
                         "Props:\n" \
                         "\thref: https://www.google.com\n" \
                         "\ttarget: _blank")
        self.assertEqual(str(node2),
                         "Tag: a\n" \
                         "Value: Value blah blah blah")
        self.assertEqual(str(node3),
                         "Tag: h1\n" \
                         "Children:\n" \
                         "\t0: Value: I'm a child!\n" \
                         "\t1: Value: I'm also a child")
     
    
    def test_props_to_html(self):
        print("***Test Props to HTML***")
        node = HTMLNode(tag="p", value="This is the value of the thing", props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

if __name__ == "__main__":
    print("-----TEST HTMLNODE------")
    unittest.main()