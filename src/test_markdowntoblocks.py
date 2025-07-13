import unittest

from mdfunctions import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        print("***Test Markdown to Blocks")
        markdown = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        #print(markdown)
        blocks = markdown_to_blocks(markdown)
        #print(blocks)
        self.assertEqual(blocks,
                         [
                             "This is **bolded** paragraph",
                             "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                             "- This is a list\n- with items",
                         ]
        )
    
    def test_get_block_type(self):
        print("***Test Get Block Type***")
        markdown = """
This is a standard paragraph block with **bolded** text

This is a standard paragraph block with multiple lines
This is the second line of the paragraph

# This is a heading block

## Also a heading block

####### Let's see what this is, hopefully a standard paragraph

```Code block
blahd
blah
blah```

- This
- Is
- An
- Unordered
- List

1. This
2. Is
3. An
4. Ordered
5. List

>Quote line one
>Quote Line two
>Quote line three

>False quote line one
Line two
>Line 3
"""
        blocks = markdown_to_blocks(markdown)
        block_types = []
        for block in blocks:
            #print(block_to_block_type(block))
            block_types.append(block_to_block_type(block))
        
        #print(block_types)
        self.assertListEqual(block_types,
                             [
                                 BlockType.PARAGRAPH,
                                 BlockType.PARAGRAPH,
                                 BlockType.HEADING,
                                 BlockType.HEADING,
                                 BlockType.PARAGRAPH,
                                 BlockType.CODE,
                                 BlockType.UNORDERED_LIST,
                                 BlockType.ORDERED_LIST,
                                 BlockType.QUOTE,
                                 BlockType.PARAGRAPH,
                             ]
        )

if __name__ == "__main__":
    print("-----TEST MARKDOWN TO BLOCKS------")
    unittest.main()