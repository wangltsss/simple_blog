---
title: Markdown Basics
date: 2021-01-01
---

# Markdown Basics and Cheat Sheet  

This blog serves as a concise summary of essential Markdown features along with a handy cheat sheet. If you're looking for an in-depth tutorial or a comprehensive guide on the advantages of using Markdown, this blog may not cover all your needs. Instead, it provides a quick reference to help you effectively utilize Markdown in your projects.

## Table of Contents

1. [Writing Text and Formatting](#writing-text-and-formatting)
2. [Lists](#lists)
3. [Including Images and Links](#including-images-and-links)
4. [Code and Syntax Highlighting](#code-and-syntax-highlighting)
5. [Adding Tables](#adding-tables)
7. [Miscellaneous](#miscellaneous)
8. [Packages and Tools](#packages-and-tools)

---


## Writing Text and Formatting

Markdown provides a variety of commands to format your text quickly:

- **Bold Text:** `**This is bold text.**`
- *Italic Text:* `*This is italic text.*`
- <ins>Underlined Text</ins>: `<u>This is underlined text.</u>`
- ~~Strikethrough Text~~: `~~This text is struck through.~~`

### Bold Text

To make text bold, wrap it with double asterisks (`**`) or double underscores (`__`).

```markdown
**This is bold text.**
```

**This is bold text.**

### Italic Text

To italicize text, wrap it with single asterisks (`*`) or single underscores (`_`).

```markdown
*This is italic text.*
```

*This is italic text.*

### Underlined Text

Markdown doesn't have a native syntax for underlining text, but you can use HTML tags within Markdown.

```markdown
<u>This is underlined text.</u>
```

<u>This is underlined text.</u>

### Strikethrough Text

To strike through text, wrap it with double tildes (`~~`).

```markdown
~~This text is struck through.~~
```

~~This text is struck through.~~

## Lists

Markdown supports various types of lists to organize your content.

### Unordered List

Use dashes (`-`), plus signs (`+`), or asterisks (`*`) to create unordered lists.

```markdown
- First item
- Second item
- Third item
```

- First item
- Second item
- Third item

### Ordered List

Use numbers followed by periods to create ordered lists.

```markdown
1. First item
2. Second item
3. Third item
```

1. First item
2. Second item
3. Third item

### Task List

Create task lists by starting each item with `- [ ]` for incomplete tasks or `- [x]` for completed tasks.

```markdown
- [ ] Task One
- [x] Task Two
- [ ] Task Three
```

- [ ] Task One
- [x] Task Two
- [ ] Task Three

## Including Images and Links

Enhance your Markdown documents by embedding images and creating hyperlinks.

### Images

Use the `![]()` syntax to include images.

```markdown
![Alt Text](path/to/image.png)
```

![Alt Text](https://via.placeholder.com/150)

### Links

Use the `[]()` syntax to create clickable links.

```markdown
[Google](https://www.google.com)
```

[Google](https://www.google.com)

## Code and Syntax Highlighting

Display code snippets or blocks with proper formatting.

### Inline Code

Wrap code with backticks (\`).

```markdown
Here is some `inline code`.
```

Here is some `inline code`.

### Code Blocks

Use triple backticks (\`\`\`) to create code blocks. Specify the language for syntax highlighting.

```markdown
```python
def hello_world():
    print("Hello, world!")
```
```

```python
def hello_world():
    print("Hello, world!")
```

## Adding Tables

Organize data in tables using pipes (`|`) and hyphens (`-`).

```markdown
| Column1 | Column2 | Column3 |
|---------|---------|---------|
| Data1   | Data2   | Data3   |
| Data4   | Data5   | Data6   |
```

| Column1 | Column2 | Column3 |
|---------|---------|---------|
| Data1   | Data2   | Data3   |
| Data4   | Data5   | Data6   |

## Markdown Cheat Sheet

Navigating Markdown's syntax can be straightforward with a handy cheat sheet. Here's a comprehensive overview of common Markdown commands to help you get up to speed quickly:

### Basic Syntax

| **Syntax**           | **Purpose**                   | **Example**                        |
|----------------------|-------------------------------|------------------------------------|
| `# Heading 1`        | Largest heading               |  # Heading 1                     |
| `## Heading 2`       | Second largest heading        | ## Heading 2                     |
| `### Heading 3`      | Third largest heading         | ### Heading 3                    |
| `**Bold Text**`      | Bold text                     | **Bold Text**                    |
| `*Italic Text*`      | Italic text                   | *Italic Text*                    |
| `~~Strikethrough~~`  | Strikethrough text            | ~~Strikethrough~~                |
| `[Link](URL)`        | Hyperlink                     | [OpenAI](https://www.openai.com)  |
| `![Alt Text](URL)`   | Image                         | ![Alt Text](https://via.placeholder.com/150) |

### Advanced Formatting

| **Syntax**             | **Purpose**                       | **Example**                                     |
|------------------------|-----------------------------------|-------------------------------------------------|
| `> Blockquote`         | Blockquote                        | > This is a blockquote.                       |
| `\` Code Span         | Inline code                       | Here is some `inline code`.                  |
| ```` ```language ```` | Code block with syntax highlighting | See Below|
```python
def hello_world():
    print("Hello, world!")
</code></pre>
```
### Lists

| **Syntax**               | **Purpose**                      | **Example**                                     |
|--------------------------|----------------------------------|-------------------------------------------------|
| `- Item` or `* Item`     | Unordered list                   | - First item                                 |
| `1. Item`                | Ordered list                     | 1. First item                                 |
| `- [ ] Task`             | Task list                        | - [ ] Incomplete Task                         |
| `- [x] Task`             | Completed task in task list      | - [x] Completed Task                           |

### Media Embedding

| **Syntax**               | **Purpose**                      | **Example**                                     |
|--------------------------|----------------------------------|-------------------------------------------------|
| `![Alt Text](URL)`       | Embed an image                   | ![Alt Text](https://via.placeholder.com/150)   |
| `[Link Text](URL)`       | Create a hyperlink               | [OpenAI](https://www.openai.com)               |
| `<u>Underlined</u>`      | Underline text (HTML)            | <u>Underlined Text</u>                         |

### Extensions and Plugins

Markdown can be extended with additional syntax and plugins for enhanced functionality.

| **Extension**            | **Purpose**                      | **Example**                                     |
|--------------------------|----------------------------------|-------------------------------------------------|
| **Tables**               | Create tables                    | See [Adding Tables](#adding-tables)              |
| **Footnotes**            | Add footnotes                    | Here is a footnote[^1].`<br>`[^1]: Footnote text. |
| **Task Lists**           | Create interactive task lists    | See [Lists](#lists)                              |
| **LaTeX Math**           | Include mathematical notation    | $E = mc^2$                                     |

### Tips for Using the Cheat Sheet

- **Copy and Paste:** Feel free to copy the examples directly into your Markdown document and modify them as needed.
- **Use Preview:** Utilize Markdown editors that offer live preview to see how your formatting appears.
- **Explore Extensions:** Enhance your Markdown experience by exploring various extensions and plugins available for your preferred editor.

## Miscellaneous

Markdown is versatile, but it has its limitations. Here are a few additional tips and tricks:

- **Line Breaks:** End a line with two spaces to create a line break.
  
  ```markdown
  First line.  
  Second line.
  ```
  
  First line.  
  Second line.

- **Horizontal Rule:** Create a horizontal line using three or more hyphens (`---`), asterisks (`***`), or underscores (`___`).

  ```markdown
  ---
  ```

  ---

- **Escaping Characters:** Use a backslash (`\`) to escape Markdown syntax characters if you want to display them as plain text.

  ```markdown
  \*This text is not italicized.\*
  ```

  \*This text is not italicized.\*

## Packages and Tools

While Markdown is simple by default, various tools and extensions can enhance its functionality:

| **Tool/Extension**      | **Purpose**                      | **Usage**                                     |
|-------------------------|----------------------------------|-----------------------------------------------|
| **Markdown Preview**    | Live preview of Markdown files   | Available in editors like VS Code, Atom, etc. |
| **Pandoc**              | Convert Markdown to various formats | `pandoc input.md -o output.pdf`               |
| **Markdownlint**        | Lint Markdown files for style consistency | Install as a plugin in your editor            |
| **GitHub Flavored Markdown (GFM)** | Enhanced Markdown features on GitHub | Automatic support on GitHub repositories      |
| **Mermaid**             | Create diagrams and flowcharts   | Use fenced code blocks with `mermaid` syntax   |
| **Typora**              | WYSIWYG Markdown editor          | Download and install from [Typora](https://typora.io/) |
