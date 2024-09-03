import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node , node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold" , "https://pizza.com")
        self.assertNotEqual(node , node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text bold", "bold")
        self.assertNotEqual(node , node2)

    def test_text_type_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node , node2)

    def test_textnode_eq_method(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        node3 = TextNode("wazz Up" , "bold", "https://Scream")
        self.assertTrue(node.__eq__(node2))
        self.assertFalse(node.__eq__(node3),"Test TextNode method for checking if two nodes are equal.")

    def test_repr(self):
        node = TextNode("This is a text node.","text","https://boot.dev")
        self.assertEqual("TextNode(This is a text node., text, https://boot.dev)", repr(node))

    def test_text_node_to_html_text(self):
        text_node = TextNode( "Hello, World!","text")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "Hello, World!")

    def test_text_node_to_html_bold(self):
        text_node = TextNode("Bold Text", "bold")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<b>Bold Text</b>")

    def test_text_node_to_html_italic(self):
        text_node = TextNode( "Italic Text","italic",)
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<i>Italic Text</i>")

    def test_text_node_to_html_code(self):
        text_node = TextNode("print('Hello')","code")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), "<code>print('Hello')</code>")

    def test_text_node_to_html_link(self):
        text_node = TextNode("Boot.dev","link", "https://www.boot.dev/tracks/backend")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<a href="https://www.boot.dev/tracks/backend">Boot.dev</a>')

    def test_text_node_to_html_image(self):
        text_node = TextNode("An image","image", "image.jpg")
        html_node = text_node.text_node_to_html_node()
        self.assertEqual(html_node.to_html(), '<img src="image.jpg" alt="An image" />')

    def test_text_node_to_html_unknown_type(self):
        text_node = TextNode("Unknown", "unknown")
        with self.assertRaises(ValueError) as context:
         text_node.text_node_to_html_node()
        self.assertEqual(str(context.exception), "Unknown text type: unknown")
    
if __name__ == "__main__":
    unittest.main()
    
