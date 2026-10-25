from textnode import TextNode, TextType
from htmlnode import LeafNode



def main():
    new_node = LeafNode("p", "This is a paragraph of text.", {
        "target": "_blank",
        "class": "h1 dark"
    })
    print(new_node.to_html())
    
main()