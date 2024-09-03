import unittest
from htmlnode import LeafNode
class TestLeafNode (unittest.TestCase):
    def test_LeafNode_values(self):
        node = LeafNode("a" , "I love Javascript I must be a little timmy",{"chad":False , "Timmy":True})
        self.assertEqual(node.tag,"a")
        self.assertEqual(node.value , "I love Javascript I must be a little timmy")
        self.assertDictEqual(node.props, {"chad":False , "Timmy":True})

    def test_LeafNode_toHtml(self):
        node = LeafNode("a" , "I love Javascript I must be a little timmy",{"chad":False , "Timmy":True})
        node2 = LeafNode(None , "I love Javascript I must be a little timmy")
        node3 = LeafNode("a" ,None ,{"chad":False , "Timmy":True}) 
        node4 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html() , '<a chad="False" Timmy="True">I love Javascript I must be a little timmy</a>')
        self.assertEqual(node2.to_html() , "I love Javascript I must be a little timmy")
        self.assertEqual(node4.to_html(), "<p>This is a paragraph of text.</p>")
        with self.assertRaises(ValueError):
            node3.to_html()