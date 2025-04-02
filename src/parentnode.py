from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag.")
        if self.children == None or len(self.children) < 1:
            raise ValueError("ParentNode must have children.")

        result = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            result += child.to_html()
        return result + f"</{self.tag}>"
    
    def __str__(self):
        return self.to_html()