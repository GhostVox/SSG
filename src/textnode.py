from htmlnode import LeafNode

class TextNode ():
    def __init__(self ,text:str , text_type:str , url:str = None ):
        self.text = text
        self.text_type = text_type
        self.url = url
        

    def __eq__(self ,node2):
        if (self.text == node2.text and
        self.text_type == node2.text_type and
        self.url == node2.url):
            return True
        return False
    
 
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
            match self.text_type:
                case "text":
                    return LeafNode(None, self.text)
                case "bold":
                    return LeafNode("b", self.text)
                case "italic":
                    return LeafNode("i", self.text)
                case "code":
                    return LeafNode("code" , self.text)
                case "link":
                    return LeafNode("a",self.text,{"href":self.url})
                case "image":
                    return LeafNode("img", "",{"src":self.url , "alt":self.text})
                case _:
                    raise ValueError(f"Unknown text type: {self.text_type}")
    
