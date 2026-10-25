from htmlnode import HTMLNode, LeafNode, ParentNode
import unittest



class TestHTMLNode(unittest.TestCase):
    def test_eq_props_to_html(self):
        node = HTMLNode("p", "This is a text node", None, {
            "class": "col-md-12",
            "target": "_blank"
        })
        node2 = HTMLNode("p", "This is a text node", None, {
            "class": "col-md-12",
            "target": "_blank"
        })
        self.assertEqual(node.props_to_html(), node2.props_to_html())

    def test_props_to_html_text(self):
        node = HTMLNode("p", "This is a text node", None, {
            "class": "col-md-12",
            "target": "_blank"
        })

        self.assertEqual(node.props_to_html(), ' class="col-md-12" target="_blank"')

    def test_not_eq(self):
        node = HTMLNode("p", "This is a text node", None, {
            "class": "col-md-12",
            "target": "_blank"
        })
        node2 = HTMLNode("p", "This is a text node", None, {
            "class": "col-md-12",
            "target": "_blank"
        })
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_tags(self):
        node = LeafNode("p", "Hello World", {
            "class": "h1 dark",
            "target": "_blank"
        })
        self.assertEqual(node.to_html(), '<p class="h1 dark" target="_blank">Hello World</p>')

    def test_leaf_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None).to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
if __name__ == "__main__":
    unittest.main()