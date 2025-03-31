import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_rawtext(self):
        example_text = "Some empty text"
        node = LeafNode(None, example_text)
        self.assertEqual(node.to_html(), example_text)
    
    def test_leaf_to_html_raises_value_error(self):
        node = LeafNode("div", None, {"id": "myDiv"})
        self.assertRaises(ValueError)
    