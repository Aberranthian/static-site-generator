import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_parent_empty_raises(self):
        node = ParentNode(None, None, None)
        self.assertRaises(ValueError, node.to_html)
    
    def test_parent_no_tag_raises(self):
        child = LeafNode("p", "Some paragraph.", {"font-size": 16})
        node = ParentNode(None, [child], {"color": "#123456"})
        self.assertRaises(ValueError, node.to_html)
    
    def test_parent_no_child_raises(self):
        node = ParentNode(None, None, {"color": "#123456"})
        self.assertRaises(ValueError, node.to_html)
    
    def test_parent_empty_list_children_raises(self):
        node = ParentNode(None, [], {"color": "#123456"})
        self.assertRaises(ValueError, node.to_html)
    
    def test_to_html_with_child_eq(self):
        child = LeafNode("p", "Some paragraph.", {"font-size": 16})
        node = ParentNode("div", [child], {"color": "#123456"})
        self.assertEqual(node.to_html(), "<div color=\"#123456\"><p font-size=\"16\">Some paragraph.</p></div>")
    
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