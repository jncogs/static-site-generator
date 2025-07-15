import unittest

from mdfunctions import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        print("*** Test Extract Markdown Title ***")
        markdown = """

this is a regular paragraph

# This is the **title**, _allegedly_, with some `code`

## Another header

# Test header

- List item 1
- List item 2
- List **item 3**
"""
        title = extract_title(markdown)
        #print(extract_title(markdown))
        self.assertEqual(title, "This is the title, allegedly, with some code")

if __name__ == "__main__":
    print("------TEST EXTRACT MARKDOWN TITLE------")
    unittest.main()