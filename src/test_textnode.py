from textnode import TextNode, TextType
import unittest


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.PLAIN)
        self.assertNotEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        self.assertEqual(node.url, None)
        
if __name__ == "__main__":
    unittest.main()