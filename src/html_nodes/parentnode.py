from html_nodes.htmlnode import *

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag")
        if self.children is None:
             raise ValueError("All parent nodes must have children")
        
        contents = functools.reduce(lambda current, child: current + child.to_html(),
            self.children, "")
        return f'<{self.tag}>{contents}</{self.tag}>'
        
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"