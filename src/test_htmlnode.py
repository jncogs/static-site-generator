import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        print("-----TEST HTMLNODE------")
        node = HTMLNode(tag="p", value="This is the value of the thing", props={"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode(tag="a", value="Value blah blah blah")
        child1 = HTMLNode(value="I'm a child!")
        child2 = HTMLNode(value="I'm also a child")
        node3 = HTMLNode(tag="h1", children=[child1, child2])

        print(f"Node 1:\n{node}")
        print(f"Node 2:\n{node2}")
        print(f"Node 3:\n{node3}")
        print(f"Child 1:\n{child1}")
        print(f"Child 2:\n{child2}")

        print(f"Props: {node.props_to_html()}")

if __name__ == "__main__":
    unittest.main()