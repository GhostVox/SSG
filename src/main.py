from textnode import TextNode
from htmlnode import HTMLNode , ParentNode ,LeafNode
from copy_static import copy_files_recursive , generate_page,generate_pages_recursive
    
def main():
    copy_files_recursive("static", "public")
    result = generate_pages_recursive("content","template.html","public")
    if result == 0:
        print("Success!!!!!")
        
    
    
    return


if __name__ == "__main__":
    main()