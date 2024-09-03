import unittest

from htmlnode import HTMLNode

class TESTHTMLNode(unittest.TestCase):
    def test_HtmlNode_creaation(self):
        node1 = HTMLNode("p","Hello World", [],{"class":"main"} )
        node2 = HTMLNode("a","Hello World", [],{"href":"https://Travman"} )
        self.assertNotEqual(node1 , node2)
    
    def test_html_repr(self):
        node1 = HTMLNode("p","Hello World", [],{"class":"main"} )
        self.assertTrue(repr(node1) == "HTMLNode(p, Hello World, children:[], {'class': 'main'})")
    
    def test_HtmlNode_props(self):
        node1 = HTMLNode("a","Hello World", [],{"class":"main" ,"href":"http://HelloWorld.com" } )
        node2 = HTMLNode("p","Javascript is the best langauge")
        self.assertTrue(node1.props_to_html() == 'class="main" href="http://HelloWorld.com"')
        self.assertTrue(node2.props_to_html() == '')                                       