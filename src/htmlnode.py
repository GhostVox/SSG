
class HTMLNode ():
    def __init__(self , tag:str=None , value:str=None , children:list=None , props:dict=None):
        self.tag = tag # e.g "p" or "div"
        self.value = value # string representation of text in tag
        self.children = children  # a list of HTMLNode objects representing the children of this node
        self.props = props  # dictionary of  Attributes of this node e.g class: "value" or href : "url..."

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return " ".join(f'{key}="{value}"' for key , value in self.props.items())
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children:{self.children}, {self.props})"
    

class LeafNode (HTMLNode):
    self_closing_elements =[
        "img"
    ]
    def __init__(self ,tag:str, value:str ,props:dict=None ):
        super().__init__(tag,value,None , props)
      
       

    def to_html(self):
        if  self.value == None and self.tag != "img":
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        closing_tag = f"</{self.tag}>"
        opening_tag = f"<{self.tag}{' ' +self.props_to_html() if self.props else ''}"
        if self.tag in self.self_closing_elements:
            return f"{opening_tag} />"
        return f"{opening_tag}>{self.value}{closing_tag}"
   
    

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self , tag:str ,children:list , props:dict = None):
        super().__init__(tag ,None, children ,props)
    
    def to_html(self):
        if  self.tag is None:
            raise ValueError("Html Tag required to make parent node.")
        if  self.children is None:
            raise ValueError("Parent node must contain children nodes.")
        result = ''
        for child in self.children:
            if isinstance(child , LeafNode):
                 result += child.to_html()
            elif isinstance(child , ParentNode):
                result += child.to_html()

        return f"<{self.tag}{' ' + self.props_to_html() if self.props else ''}>{result}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, props: {self.props} )"