import unittest

from inline_markdown import (split_nodes_delimiter , 
                             extract_markdown_links,
                             extract_markdown_images,
                             split_node_link , 
                             split_node_image , 
                             text_to_textnodes,
                             text_type_bold,
                             text_type_code,
                             text_type_image,
                             text_type_italic,
                             text_type_link,
                             text_type_text
                             )
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
        result = split_nodes_delimiter([text_node],None, "text")
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
        
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
       
        self.assertEqual([("rick roll" , 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan','https://i.imgur.com/fJRm4Vk.jpeg')],extract_markdown_images(text))
        

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual([("to boot dev" , "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], extract_markdown_links(text))
    
    def test_split_node_link(self):
        node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    "text",
)
        expect = [
        TextNode("This is text with a link ", "text"),
        TextNode("to boot dev", "link", "https://www.boot.dev"),
        TextNode(" and ", "text"),
        TextNode(
         "to youtube", "link", "https://www.youtube.com/@bootdotdev"
     ),
    ]
        self.assertEqual(expect , split_node_link([node]))
        
    def test_split_node_image(self):
        node = TextNode("This is a text node with that has a ![image of a cat](https://catsareus) in it.","text")
        node2 = TextNode("This is a text node with that has a ![image of a cat](https://catsareus) in it and a ![image of a dog](https://dogsareus).","text")
        node3 = TextNode("This node has no image.","text")
        expect = [
            TextNode("This is a text node with that has a ","text"),
            TextNode("image of a cat","image","https://catsareus"),
            TextNode(" in it.","text")
        ]
        expect2 = [  
            TextNode("This is a text node with that has a ","text"),
            TextNode("image of a cat","image","https://catsareus"),
            TextNode(" in it and a ","text"),
            TextNode("image of a dog","image","https://dogsareus"),
            TextNode(".","text")]
        self.assertEqual(expect,split_node_image([node]))
        
        self.assertEqual(expect2,split_node_image([node2]))
        self.assertEqual([TextNode("This node has no image.",'text')], split_node_image([node3]))
        
    def test_text_to_textnode(self):
        string = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expect=[
    TextNode("This is ", text_type_text),
    TextNode("text", text_type_bold),
    TextNode(" with an ", text_type_text),
    TextNode("italic", text_type_italic),
    TextNode(" word and a ", text_type_text),
    TextNode("code block", text_type_code),
    TextNode(" and an ", text_type_text),
    TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
    TextNode(" and a ", text_type_text),
    TextNode("link", text_type_link, "https://boot.dev"),
]
        self.assertEqual(expect , text_to_textnodes(string))
        
        string2 = "hello mate how are *you* today?"
        expect2 = [
            TextNode('hello mate how are ', "text"),
            TextNode('you','italic'),
            TextNode(' today?', "text")
        ]
        self.assertEqual(expect2 , text_to_textnodes(string2))
        
       # space should be respected.
        self.assertEqual([TextNode(' ', "text")],text_to_textnodes(" "))
        
        # single delimited node
        self.assertEqual([TextNode("Scooby doo was the best cartoon growing up.",'bold')], text_to_textnodes('**Scooby doo was the best cartoon growing up.**'))