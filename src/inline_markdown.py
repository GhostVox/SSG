from textnode import TextNode

text_type_text= 'text'
text_type_bold = 'bold'
text_type_italic= 'italic'
text_type_code= 'code'
text_type_link = "link"
text_type_image = "image"


def split_nodes_delimiter(old_nodes:list , delimiter:str, text_type:str) -> list:
    new_nodes = []
    
    for node in old_nodes:
        
        if not isinstance(node , TextNode) or node.text_type != text_type_text:
            new_nodes.append(node)
        
        split_list = node.text.split(delimiter)
        
        if len(split_list) == 1 or delimiter is None:
            new_nodes.append(node)
            continue
        if len(split_list) % 2 == 0:
             raise Exception("Invalid markdown syntax")
        for i in range( len(split_list)):
            if split_list[i] == "":
              continue
            if i % 2 == 0 :
                new_nodes.append(TextNode(split_list[i], text_type_text))
            else: 
                new_nodes.append(TextNode(split_list[i],text_type))
    return new_nodes        