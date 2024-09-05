import unittest

from block_markdown import markdown_to_blocks, block_to_block_type,markdown_to_html_node

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        markdown_string = f'''
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item'''
        
        
        expect = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                  '* This is the first list item in a list block\n        * This is a list item\n        * This is another list item']
       
        self.assertEqual(expect , markdown_to_blocks(markdown_string))
    
    def test_empty_markdown(self):
        markdown_string = ""
        expect = []
        self.assertEqual(expect, markdown_to_blocks(markdown_string))
    
    def test_single_line(self):
        markdown_string = "This is a single line of text."
        expect = ["This is a single line of text."]
        self.assertEqual(expect, markdown_to_blocks(markdown_string))
        
    def test_multiple_paragraphs_with_extra_newlines(self):
        markdown_string = "First paragraph.\n\n\nSecond paragraph with extra newlines.\n\nThird paragraph."
        expect = ["First paragraph.", "Second paragraph with extra newlines.", "Third paragraph."]
        self.assertEqual(expect, markdown_to_blocks(markdown_string))

    def test_paragraph_block(self):
        block = 'This is a paragraph block of text in markdown.'
        block_type = block_to_block_type(block)
        self.assertEqual("paragraph" , block_type)

    def test_heading_1_block(self):
        block = '# This is a level one heading block'
        block_type = block_to_block_type(block)
        self.assertEqual('heading 1' , block_type)
    def test_heading_2_block(self):
        block = '## This is a level one heading block'
        block_type = block_to_block_type(block)
        self.assertEqual('heading 2' , block_type)
    def test_heading_3_block(self):
        block = '### This is a level three heading block'
        block_type = block_to_block_type(block)
        self.assertEqual('heading 3' , block_type)
    def test_heading_block_to_high(self):
        block = '####### This is a level one heading block'
        with self.assertRaises(ValueError):
             block_to_block_type(block)
    def test_incorrect_heading_format(self):
        block = '#wazup'
        with self.assertRaises(ValueError):
            block_to_block_type(block)
    
    def test_code_block(self):
        block = '```whats up my guys```'
        self.assertEqual('code', block_to_block_type(block))
        
    def test_quote_block(self):
        block = '>this is a quote block.'
        self.assertEqual('quote', block_to_block_type(block))
        
    def test_unordered_list(self):
        block = '- this is a unordered block'
        block2 = '* this is also a unorderd block'
        self.assertEqual('unordered_list', block_to_block_type(block))
        self.assertEqual('unordered_list', block_to_block_type(block2))
        
    def test_ordered_list(self):
        block = '1. this is a ordered block'
        self.assertEqual('ordered_list', block_to_block_type(block))
        
    
    def test_paragraph(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with *italic* text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_lists(self):
        md = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_headings(self):
        md = """
# this is an h1

this is paragraph text

## this is an h2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )

    def test_blockquote(self):
        md = """
> This is a
> blockquote block

this is paragraph text

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )