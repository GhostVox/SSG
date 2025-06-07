# Static Site Generator

A Python-based static site generator that converts Markdown files into a complete HTML website. This project was created as part of the [Boot.dev](https://www.boot.dev) curriculum and demonstrates advanced Python programming concepts including parsing, HTML generation, and recursive algorithms.

## Features

- **Markdown to HTML Conversion** - Full support for standard Markdown syntax
- **Template System** - Use HTML templates with placeholder substitution
- **Recursive Directory Processing** - Automatically processes nested content directories
- **Static Asset Copying** - Copies CSS, images, and other static files
- **Live Development Server** - Built-in HTTP server for testing
- **Comprehensive Testing** - Extensive unit tests for all components
- **Modular Architecture** - Clean separation of concerns with focused modules

## Supported Markdown Features

### Text Formatting

- **Bold text** with `**text**` or `__text__`
- _Italic text_ with `*text*` or `_text_`
- `Inline code` with backticks
- [Links](https://example.com) with `[text](url)`
- ![Images](image.jpg) with `![alt](src)`

### Block Elements

- # Headings (H1-H6) with `#` to `######`
- Paragraphs (automatic)
- > Blockquotes with `>`
- Unordered lists with `*` or `-`
- Ordered lists with `1.` `2.` etc.
- Code blocks with triple backticks

## Project Structure

```
static_site_generator/
├── src/                          # Source code
│   ├── main.py                   # Application entry point
│   ├── textnode.py              # Text node representation
│   ├── htmlnode.py              # HTML node classes
│   ├── inline_markdown.py       # Inline markdown parsing
│   ├── block_markdown.py        # Block markdown parsing
│   ├── copy_static.py           # File operations and generation
│   └── test_*.py                # Comprehensive test suite
├── content/                     # Markdown content files
│   ├── index.md                 # Homepage content
│   └── majesty/
│       └── index.md             # Blog post example
├── static/                      # Static assets (CSS, images, etc.)
├── public/                      # Generated website output
├── template.html                # HTML template with placeholders
├── main.sh                      # Build and serve script
├── test.sh                      # Test runner script
└── README.md                    # This file
```

## Quick Start

### Prerequisites

- **Python 3.6+** - Download from [python.org](https://python.org)
- **No external dependencies** - Uses only Python standard library

### Installation & Usage

1. **Clone the repository**

   ```bash
   git clone [your-repo-url]
   cd static_site_generator
   ```

2. **Build and serve the site**

   ```bash
   chmod +x main.sh
   ./main.sh
   ```

   This will:

   - Generate the static site in the `public/` directory
   - Start a local development server on `http://localhost:8888`

3. **Manual build** (optional)

   ```bash
   python3 src/main.py
   ```

4. **Run tests**
   ```bash
   chmod +x test.sh
   ./test.sh
   ```

## Content Creation

### Adding New Pages

1. **Create a markdown file** in the `content/` directory:

   ```bash
   # For a top-level page
   echo "# My New Page" > content/about.md

   # For a nested page
   mkdir content/blog
   echo "# My Blog Post" > content/blog/my-post.md
   ```

2. **Add content** using standard Markdown syntax:

   ```markdown
   # Page Title

   This is a paragraph with **bold** and _italic_ text.

   ## Section Header

   - List item 1
   - List item 2

   [Link to Boot.dev](https://boot.dev)

   ![Image description](/images/photo.jpg)
   ```

3. **Rebuild the site**:
   ```bash
   ./main.sh
   ```

### Template Customization

Edit `template.html` to customize your site's layout:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet" />
  </head>
  <body>
    <article>{{ Content }}</article>
  </body>
</html>
```

**Available placeholders:**

- `{{ Title }}` - Automatically extracted from the first H1 heading
- `{{ Content }}` - Generated HTML content from markdown

### Static Assets

Place CSS, images, and other static files in the `static/` directory:

```
static/
├── index.css          # Main stylesheet
├── images/
│   ├── logo.png
│   └── background.jpg
└── js/
    └── script.js
```

These files are automatically copied to the `public/` directory during build.

## Architecture Overview

### Core Components

**TextNode** (`textnode.py`)

- Represents individual text elements with type information
- Handles conversion from text nodes to HTML nodes
- Supports text, bold, italic, code, links, and images

**HTMLNode Classes** (`htmlnode.py`)

- `HTMLNode`: Base class for all HTML elements
- `LeafNode`: Self-closing or simple content nodes (e.g., `<p>`, `<img>`)
- `ParentNode`: Container nodes with children (e.g., `<div>`, `<ul>`)

**Inline Parsing** (`inline_markdown.py`)

- Processes inline markdown syntax (bold, italic, code, links, images)
- Uses regular expressions for pattern matching
- Splits text nodes based on delimiters

**Block Parsing** (`block_markdown.py`)

- Handles block-level markdown elements
- Converts markdown blocks to HTML nodes
- Supports headings, paragraphs, lists, quotes, and code blocks

**Site Generation** (`copy_static.py`)

- Recursively processes content directories
- Copies static assets
- Generates HTML pages from markdown using templates

### Processing Pipeline

1. **Parse Markdown** → TextNodes → HTMLNodes
2. **Apply Template** → Insert content and title
3. **Generate HTML** → Write to public directory
4. **Copy Assets** → Static files to public directory

## Testing

The project includes comprehensive unit tests covering all functionality:

```bash
# Run all tests
./test.sh

# Run specific test modules
python3 -m unittest src.test_textnode
python3 -m unittest src.test_block_markdown
python3 -m unittest src.test_inline_markdown

# Run with verbose output
python3 -m unittest discover -s src -v
```

### Test Coverage

- **TextNode functionality** - Text representation and HTML conversion
- **HTML node generation** - Proper HTML structure and attributes
- **Markdown parsing** - All supported markdown syntax
- **Block processing** - Headings, lists, quotes, code blocks
- **Inline processing** - Bold, italic, code, links, images
- **File operations** - Directory copying and page generation

## Configuration

### Customizing Build Behavior

Modify `src/main.py` to change build settings:

```python
def main():
    # Copy static assets
    copy_files_recursive("static", "public")

    # Generate pages from content
    result = generate_pages_recursive("content", "template.html", "public")

    if result == 0:
        print("Success!!!!!")
```

### Development Server

The built-in server (started by `main.sh`) serves the site locally:

- **URL**: `http://localhost:8888`
- **Port**: 8888 (modify in `main.sh` if needed)
- **Auto-reload**: Restart the script to see changes

## Markdown Processing Details

### Inline Elements Processing Order

1. **Bold text** (`**text**`)
2. **Italic text** (`*text*`)
3. **Code spans** (`` `code` ``)
4. **Images** (`![alt](src)`)
5. **Links** (`[text](url)`)

### Block Elements Recognition

- **Headings**: Lines starting with 1-6 `#` characters
- **Code blocks**: Text wrapped in triple backticks
- **Quotes**: Lines starting with `>`
- **Unordered lists**: Lines starting with `*` or `-`
- **Ordered lists**: Lines starting with numbers and periods
- **Paragraphs**: Everything else (default)

## Learning Objectives

This project demonstrates key programming concepts:

- **Parsing and Lexical Analysis** - Converting text to structured data
- **Abstract Syntax Trees** - Representing document structure
- **Recursive Algorithms** - Processing nested directory structures
- **Object-Oriented Design** - Clean class hierarchies and interfaces
- **Template Processing** - Dynamic content generation
- **File System Operations** - Directory traversal and file manipulation
- **Regular Expressions** - Pattern matching for markdown syntax
- **Unit Testing** - Comprehensive test coverage and TDD practices
- **Modular Architecture** - Separation of concerns and code organization

## Troubleshooting

### Common Issues

**"Permission denied" when running scripts**

```bash
chmod +x main.sh test.sh
```

**Server not accessible**

- Check if port 8888 is available
- Try a different port by modifying `main.sh`
- Ensure firewall isn't blocking the connection

**Markdown not converting properly**

- Check that H1 headings start with `# ` (space after hash)
- Ensure proper spacing around markdown syntax
- Review test files for expected format examples

**Missing images or CSS**

- Verify files are in the `static/` directory
- Check file paths in markdown (should start with `/`)
- Ensure build completed successfully

**Template placeholders not replaced**

- Verify template uses `{{ Title }}` and `{{ Content }}` exactly
- Check that markdown files have H1 headings for title extraction

## Future Enhancements

Potential improvements you could add:

- **Syntax highlighting** for code blocks
- **Custom CSS themes** and template system
- **RSS feed generation** for blog functionality
- **Image optimization** and responsive handling
- **Search functionality** with client-side indexing
- **Hot reload** for development server
- **Deployment scripts** for hosting platforms
- **Custom markdown extensions** (tables, footnotes, etc.)

Perfect for Python developers interested in learning about parsing, HTML generation, and building complete web development tools from scratch!
