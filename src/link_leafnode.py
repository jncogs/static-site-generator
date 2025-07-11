from htmlnode import HTMLNode

class LinkLeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        props = []
        for prop in self.props:
            props.append(f"{prop}=\"{self.props[prop]}\"")
        return f"<{self.tag} {" ".join(props)}>{self.value}</{self.tag}>"