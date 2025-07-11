from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        output = []

        if not self.tag:
            raise ValueError("No tag given")
        if not self.children:
            raise ValueError("No children")
        
        for child in self.children:
            output.append(child.to_html())

        return f"<{self.tag}>{"".join(output)}</{self.tag}>"