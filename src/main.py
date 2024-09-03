from textnode import TextNode
from htmlnode import HTMLNode , ParentNode ,LeafNode
def main():
        children = [

            LeafNode("h1", "Welcome to My Website", {"class": "header"}),
            LeafNode("p", "This is a paragraph with some text.", {"class": "text-paragraph"}),
            LeafNode("img", None, {"src": "image.jpg", "alt": "An image"}),
            LeafNode("a", "Click here", {"href": "https://example.com", "class": "link-button"}),
        ]
        node = ParentNode("div", children,{"class":"container"})
        print(node.to_html())
        return 
if __name__ == "__main__":
    main()