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

if __name__ == "__main__":
    unittest.main()
    
