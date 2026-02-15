from text_functions.markdown_to_html_node import *
import unittest

### heading
### paragraph
### quote
## code
## orderd list
## unorderd list



class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_quote(self):
        md = """
> Quote here
> More quote
> Even More quote
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quote here More quote Even More quote</blockquote></div>",
        )
    
    def test_heading_1(self):
        md = """
# Heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Heading</h1></div>",
        )

    def test_heading_2_bold(self):
        md = """
## **Heading**
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2><b>Heading</b></h2></div>",
        )

    def test_heading_3(self):
        md = """
### Heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Heading</h3></div>",
        )
    def test_heading_4(self):
        md = """
#### Heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h4>Heading</h4></div>",
        )
    def test_heading_5(self):
        md = """
##### Heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h5>Heading</h5></div>",
        )
    def test_heading_6(self):
        md = """
###### Heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>Heading</h6></div>",
        )
    def test_heading_7_paragraph(self):
        md = """
####### Heading
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### Heading</p></div>",
        )

    def test_ordered_list(self):
        md = """
1. Test
2. List
3. Here
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Test</li><li>List</li><li>Here</li></ol></div>",
        )
    def test_ordered_list_attributes(self):
        md = """
1. Test **bold**
2. List _italic_
3. Here `code`
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>Test <b>bold</b></li><li>List <i>italic</i></li><li>Here <code>code</code></li></ol></div>",
        )
    
    
    def test_unordered_list(self):
        md = """
- Test
- List
- Here
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Test</li><li>List</li><li>Here</li></ul></div>",
        )
    def test_unordered_list_attributes(self):
        md = """
- Test **bold**
- List _italic_
- Here `code`
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>Test <b>bold</b></li><li>List <i>italic</i></li><li>Here <code>code</code></li></ul></div>",
        )

    def test_all(self):
        md = """
# Heading 1

**paragraph** _text_ `here`

> Greatest Quote
> Of **all** time

```
some code
here
```

## Heading 2

- Chaos
- Here

1. Against
2. Order
3. World
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        print()
        print(html)
        print()
        self.assertEqual(
            html,
            "<div><h1>Heading 1</h1><p><b>paragraph</b> <i>text</i> <code>here</code></p><blockquote>Greatest Quote Of <b>all</b> time</blockquote><pre><code>some code\nhere\n</code></pre><h2>Heading 2</h2><ul><li>Chaos</li><li>Here</li></ul><ol><li>Against</li><li>Order</li><li>World</li></ol></div>"
        )