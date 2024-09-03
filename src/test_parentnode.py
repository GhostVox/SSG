import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode (unittest.TestCase):

    children = [

        LeafNode("h1", "Welcome to My Website", {"class": "header"}),
        LeafNode("p", "This is a paragraph with some text.", {"class": "text-paragraph"}),
        LeafNode("img", '', {"src": "image.jpg", "alt": "An image"}),
        LeafNode("a", "Click here", {"href": "https://example.com", "class": "link-button"}),
    ]

    children2 = [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

    props = {
        "class":"container"
        
    }

    def test_parentnode_values(self):
        node = ParentNode("div",[self.children[0]] , self.props.copy())
        self.assertEqual(node.__repr__(), "ParentNode(div, children: [LeafNode(h1, Welcome to My Website, {'class': 'header'})], props: {'class': 'container'} )")

    def test_parentnode_tohtml(self):
        node = ParentNode("div", self.children , self.props.copy())
        node2 = ParentNode("p", self.children2 )
        node3 = ParentNode("div",[self.children[1]] )
        node4 = ParentNode("div",[self.children[1]] )
        node3.children = None
        node4.tag = None
        self.assertEqual(node.to_html() , '<div class="container"><h1 class="header">Welcome to My Website</h1><p class="text-paragraph">This is a paragraph with some text.</p><img src="image.jpg" alt="An image"></img><a href="https://example.com" class="link-button">Click here</a></div>')
        self.assertEqual(node2.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')
        with self.assertRaises(ValueError):
            node3.to_html()
        with self.assertRaises(ValueError):
            node4.to_html()
    

