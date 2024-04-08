import unittest
from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HtmlNode("div", "Hello, world!", None, {"class": "greeting", "href": "https://boot.dev"})
        self.assertEqual(node.props_to_html(), ' class="greeting" href="https://boot.dev"')
    
    def test_to_html_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
    
    def test_to_html_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')


if __name__ == "__main__":
    unittest.main()