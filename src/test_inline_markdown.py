import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode
italic_node = TextNode('hi I am a text node with a *italic word in the* node',"text")

bold_node = TextNode('hi I am text node with a **bold word in the** node',"text")

text_node = TextNode('Hello im a regular text node', "text")

code_node = TextNode("Ello mate im a text node with ```Code in the``` node","text")

list_of_nodes = [text_node,bold_node,italic_node,code_node]
class TestSplitNodesDelimiter(unittest.TestCase):
    
    def test_text_node(self):
        # No delimiter in the text node, so it should return the node unchanged
        expected = [TextNode('Hello im a regular text node', 'text')]
        result = split_nodes_delimiter([text_node], None, "text")
        self.assertEqual(expected, result)
      
    def test_italic_node(self):
        # Test splitting an italic node
        expected = [
            TextNode("hi I am a text node with a ", "text"),
            TextNode("italic word in the", "italic"),
            TextNode(" node", "text")
        ]
        result = split_nodes_delimiter([italic_node], "*", "italic")
        self.assertEqual(expected, result)

    def test_bold_node(self):
        # Test splitting a bold node
        expected = [
            TextNode("hi I am text node with a ", "text"),
            TextNode("bold word in the", "bold"),
            TextNode(" node", "text")
        ]
        result = split_nodes_delimiter([bold_node], "**", "bold")
        self.assertEqual(expected, result)
    
    def test_code_node(self):
        # Test splitting a code node
        expected = [
            TextNode("Ello mate im a text node with ", "text"),
            TextNode("Code in the", "code"),
            TextNode(" node", "text")
        ]
        result = split_nodes_delimiter([code_node], "```", "code")
        self.assertEqual(expected, result)