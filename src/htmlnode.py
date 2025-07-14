class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        child_output = []
        
        if not self.value and not self.children:
            raise ValueError("HTMLNode contains no value or children")
        if self.children:
            for child in self.children:
                child_output.append(child.to_html())
            output = "".join(child_output)
        else:
            output = self.value

        if self.tag:
            return f"<{self.tag}>{output}</{self.tag}>"
        return output
    
    def props_to_html(self):
        output_list = []

        if self.props:
            for prop in self.props:
                key = prop
                value = self.props[key]
                output_list.append(f"{key}=\"{value}\"")
        
        return " ".join(output_list)

    def __repr__(self):
        output = []
        if self.tag:
            output.append(f"Tag: {self.tag}")
        if self.value:
            output.append(f"Value: {self.value}")
        if self.children:
            output.append("Children:")
            for child in self.children:
                output.append(f"\t{self.children.index(child)}: {child}")
            #output.append(f"Children: {self.children}")
        if self.props:
            output.append("Props:")
            #output.append(f"Props: {self.props}")
            for prop in self.props:
                output.append(f"\t{prop}: {self.props[prop]}")
        
        return "\n".join(output)