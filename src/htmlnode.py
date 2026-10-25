class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        formatted_string = ""
        if self.props is not None:
            for k,v in self.props.items():
                formatted_string += f' {k}="{v}"'
            return formatted_string
        return ""

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError

        if self.tag is None:
            return f"{self.value}"

        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag = tag, value=None, children = children, props = props)

    def to_html(self):
        if self.tag is None:
            raise ValueError

        if self.children is None:
            raise ValueError("No children present in parent node")

        start = f"<{self.tag}{self.props_to_html()}>"
        end = f"</{self.tag}>"
        body = ""
        for child in self.children:
            child_body = child.to_html()
            body += child_body
        return start + body + end

        