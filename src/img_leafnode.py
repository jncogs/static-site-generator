from htmlnode import HTMLNode

class ImgLeafNode(HTMLNode):
    def __init__(self, tag, props):
        super().__init__(tag, None, None, props)
    
    def to_html(self):
        props = []
        for prop in self.props:
            props.append(f"{prop}=\"{self.props[prop]}\"")
        return f"<{self.tag} {" ".join(props)} />"