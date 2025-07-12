import unittest

from mdfunctions import markdown_to_blocks

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

if __name__ == "__main__":
    print("-----TEST MARKDOWN TO BLOCKS------")
    unittest.main()