from textnode import TextNode
from re import findall
text_type_text= 'text'
text_type_bold = 'bold'
text_type_italic= 'italic'
text_type_code= 'code'
text_type_link = "link"
text_type_image = "image"


def split_nodes_delimiter(old_nodes:list, delimiter:str, text_type:str)->list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text or delimiter is None:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes     


def extract_markdown_images(text:str)->list[tuple]:
    images = findall(r"!\[(.*?)\]\((.*?)\)",text)
    return images

def extract_markdown_links(text:str)->list[tuple]:
    links = findall(r"\[(.*?)\]\((.*?)\)",text)
    return links

def split_node_image(old_nodes:list)->list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        remaining_text = node.text
        for image in images:
            image_alt_text = image[0]
            image_url = image[1] 
            node_split = remaining_text.split(f"![{image_alt_text}]({image_url})", 1)
            if node_split[0]:
                new_nodes.append(TextNode(node_split[0],text_type_text))
            new_nodes.append(TextNode(image_alt_text,"image",image_url))
            remaining_text = node_split[1] if node_split[1] else ""
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,"text"))
    return new_nodes

def split_node_link(old_nodes:list) ->list[TextNode]:
    new_nodes = []
    
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        if len(links) == 0 :
            new_nodes.append(old_node)
            continue
        remaining_text = old_node.text
        for link in links:
            text = link[0]
            href = link[1]
            split_parts = remaining_text.split(f"[{text}]({href})",1)
            if split_parts[0]:
                new_nodes.append(TextNode(split_parts[0],text_type_text))
            new_nodes.append(TextNode(link[0],text_type_link,link[1]))
            remaining_text = split_parts[1] if len(split_parts) > 1 else ""
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text,text_type_text))
            
    return new_nodes

def text_to_textnodes(string:str) ->list[TextNode]:
    node = TextNode(string,"text")
    updated_node_list = []
    updated_node_list = split_nodes_delimiter([node],"**" , text_type_bold)
    updated_node_list = split_nodes_delimiter(updated_node_list,"*" , text_type_italic)
    updated_node_list = split_nodes_delimiter(updated_node_list,"`",text_type_code)
    updated_node_list = split_node_image(updated_node_list)
    updated_node_list = split_node_link(updated_node_list)
    return updated_node_list
    