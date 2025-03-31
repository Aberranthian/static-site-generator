class HTMLNode:
    ### An HTMLNode is assumed to have a value if no children or
    ### children if no value.
    def __init__(
            self, 
            tag = None, # string
            value = None, # string
            children = None, # HTMLNode list
            props = None # string dict
            ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    ### Children will override this method to render
    ### themselves as html.
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if self.props == None:
            return ""
        result = ""
        for key,val in self.props.items():
            result += f" {key}=\"{val}\""
        return result

    def __repr__(self):
        return f"HTMLNode(tag={self.tag},value={self.value},children={self.children},props={self.props})"