import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_valid_node(self):
        node = HTMLNode("br")
        self.assertTrue(
            node.tag or node.value or node.children
        )
    
    def test_invalid_node(self):
        node = HTMLNode()
        self.assertFalse(
            node.tag or node.value or node.children
        )
    def test_no_props_returns_empty(self):
        node = HTMLNode("p", None, None, None)
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()