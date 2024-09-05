from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes


def markdown_to_blocks(markdown:str)->list[str]:
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks
            
            
            
#Helper function
def count_heading_level(s:str)->int:
    if not s.startswith('#') :
        return 0
    return 1 + count_heading_level(s[1:])           
            
def block_to_block_type(block:str)->str:
    block_type = "paragraph"
    
    if block.startswith('#') :
        
        result =  count_heading_level(block)
        if result > 6:
            raise ValueError("Incorrect heading level. Heading are 1-6 notated by number of # before text.")
        elif len(block) < result or block[result] is not  " ":
            raise ValueError('Heading format incorrect.')
        block_type = f"heading {result}"
        
    elif block.startswith( "```") and block.endswith("```")  :
        block_type = "code"
    elif all( line.startswith(">") for line in block.split('\n') ):
        block_type = "quote"
    elif all(line.startswith("- ") or line.startswith('* ') for line in block.split("\n")):
        block_type ="unordered_list"
    elif  all(line.split(". ")[0].isdigit() and line.split(". ")[1] for line in block.split("\n")):
        block_type = 'ordered_list'
   
    
    return block_type


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block: str) -> ParentNode:
    block_type = block_to_block_type(block)
    if block_type == 'paragraph':
        return paragraph_to_html_node(block)
    elif block_type.startswith('heading'):
        return heading_to_html_node(block)
    elif block_type == 'code':
        return code_to_html_node(block)
    elif block_type == 'ordered_list':
        return olist_to_html_node(block)
    elif block_type == 'unordered_list':
        return ulist_to_html_node(block)
    elif block_type == 'quote':
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text: str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node.text_node_to_html_node()
        children.append(html_node)
    return children


def paragraph_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    paragraph = " ".join(" ".join(lines).split())
    if paragraph:
        children = text_to_children(paragraph)
        return ParentNode("p", children, None)


def heading_to_html_node(block: str) -> ParentNode:
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level < 1 or level > 6:
        raise ValueError(f"Invalid heading level: {level}")
    
    text = block[level:].strip()
    children = text_to_children(text)
    return ParentNode(f"h{level}", children, None)


def code_to_html_node(block: str) -> ParentNode:
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block format")
    
    text = block[3:-3].strip()  # Strip ``` from both ends
    code_node = ParentNode("code", [LeafNode("text",text)], None)
    return ParentNode("pre", [code_node], None)


def olist_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        if len(item) < 3 or not item[0].isdigit() or item[1] != ".":
            continue
        text = item[3:].strip()  # Strip "1. " or "2. " etc.
        children = text_to_children(text)
        html_items.append(ParentNode("li", children, None))
    return ParentNode("ol", html_items, None)


def ulist_to_html_node(block: str) -> ParentNode:
    items = block.split("\n")
    html_items = []
    for item in items:
        if not item.startswith(("- ", "* ")):
            continue
        text = item[2:].strip()  # Strip "- " or "* "
        children = text_to_children(text)
        html_items.append(ParentNode("li", children, None))
    return ParentNode("ul", html_items, None)


def quote_to_html_node(block: str) -> ParentNode:
    lines = block.split("\n")
    new_lines = [line.lstrip("> ").strip() for line in lines if line.startswith(">")]
    content = " ".join(new_lines).strip()
    children = text_to_children(content)
    return ParentNode("blockquote", children, None)


