import unittest

from htmlfunctions import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_html(self):
        print("***Test Markdown to HTML***")
        markdown = """
# This is a test of the conversion function

This is a standard paragraph with some **BOLD** text and even some _italic_ text.
Why not also throw in some basic `code as well?` **bold**

## This heading has _italic_ in it

### Below is an unordered list

- Here is the first item
- Here is the second with an ![image](https://en.wikipedia.org/wiki/Obi-Wan_Kenobi#/media/File:Ben_Kenobi.png) of **Obi Wan**
- One last item with a [link to the wiki article](https://en.wikipedia.org/wiki/Obi-Wan_Kenobi)

### Below is a _numbered_ list:

1. First item
2. Second item
3. You **better** believe this is a third item

#### Code Time!

```This is a full code block with all kinds of **cool** formatting
Even some _italic_ if you can believe it
Here is an ![image test](https://en.wikipedia.org/wiki/Obi-Wan_Kenobi#/media/File:Ben_Kenobi.png)```

Finally, just some boring ol' quotes:

>Here is the first quote
>And the second quote
>And the third quote
"""
        test = """<div><h1>This is a test of the conversion function</h1><p>This is a standard paragraph with some <b>BOLD</b> text and even some <i>italic</i> text.
Why not also throw in some basic <code>code as well?</code> <b>bold</b></p><h2>This heading has <i>italic</i> in it</h2><h3>Below is an unordered list</h3><ul><li>Here is the first item</li><li>Here is the second with an <img src="https://en.wikipedia.org/wiki/Obi-Wan_Kenobi#/media/File:Ben_Kenobi.png" alt="image" /> of <b>Obi Wan</b></li><li>One last item with a <a href="https://en.wikipedia.org/wiki/Obi-Wan_Kenobi">link to the wiki article</a></li></ul><h3>Below is a <i>numbered</i> list:</h3><ol><li>First item</li><li>Second item</li><li>You <b>better</b> believe this is a third item</li></ol><h4>Code Time!</h4><pre><code>This is a full code block with all kinds of **cool** formatting
Even some _italic_ if you can believe it
Here is an ![image test](https://en.wikipedia.org/wiki/Obi-Wan_Kenobi#/media/File:Ben_Kenobi.png)</code></pre><p>Finally, just some boring ol' quotes:</p><blockquote>Here is the first quote<br>And the second quote<br>And the third quote</blockquote></div>"""

        final_node = markdown_to_html_node(markdown)
        #print(final_node.to_html())
        self.maxDiff=None
        self.assertEqual(final_node.to_html(), test)

if __name__ == "__main__":
    print("------TEST MARKDOWN TO HTML------")
    unittest.main()