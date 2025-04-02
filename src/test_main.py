import unittest

from textnode import *
from main import text_node_to_html_node

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_text(self):
        node = TextNode("Some filler text.", TextType.TEXT)
        converted = text_node_to_html_node(node)
        self.assertEqual(converted.tag, None)
        self.assertEqual(converted.value, node.text)
        self.assertEqual(converted.props, None)
    
    def test_text_node_to_img(self):
        node = TextNode("An image of a cat.", TextType.IMAGE, "uuu.somesite.abc")
        converted = text_node_to_html_node(node)
        self.assertEqual(converted.tag, "img")
        self.assertEqual(converted.props_to_html(), " src=\"uuu.somesite.abc\" alt=\"An image of a cat.\"")
    
    def test_text_node_to_bold(self):
        node = TextNode("An image of a cat.", TextType.BOLD)
        converted = text_node_to_html_node(node)
        self.assertEqual(converted.tag, "b")
        self.assertEqual(converted.value, node.text)
    
    def test_text_node_to_italic(self):
        node = TextNode("An image of a cat.", TextType.ITALIC)
        converted = text_node_to_html_node(node)
        self.assertEqual(converted.tag, "i")
        self.assertEqual(converted.value, node.text)
    
    def test_text_node_to_code(self):
        node = TextNode("const f = m*a", TextType.CODE)
        converted = text_node_to_html_node(node)
        self.assertEqual(converted.tag, "code")
        self.assertEqual(converted.value, node.text)
    
    def test_text_node_to_link(self):
        node = TextNode("Click Me!", TextType.LINK, "https://www.google.com")
        converted = text_node_to_html_node(node)
        self.assertEqual(converted.tag, "a")
        self.assertEqual(converted.value, node.text)
        self.assertEqual(converted.props_to_html(), " href=\"https://www.google.com\"")