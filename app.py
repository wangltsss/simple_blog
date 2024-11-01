# app.py

from flask import Flask, render_template, abort
import os
import frontmatter  # Using python-frontmatter to parse front matter
from datetime import datetime
import re  # For additional text processing if needed
from markdown_it import MarkdownIt
from mdit_py_plugins.tasklists import tasklists_plugin
from mdit_py_plugins.footnote import footnote_plugin

app = Flask(__name__)

md = MarkdownIt("gfm-like", {"html": False, "linkify": True, "typographer": True}).use(tasklists_plugin).enable("table").use(footnote_plugin)
md.enable(["linkify"])

POSTS_DIR = 'posts'

def get_post_list():
    """Get a list of all post slugs."""
    posts = []
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(POSTS_DIR, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
                # Split content into lines
                lines = post.content.split('\n')
                # Initialize excerpt
                excerpt_lines = []
                word_count = 0
                # Iterate through lines to build excerpt
                for line in lines:
                    # Skip header lines (lines starting with one or more '#')
                    if re.match(r'^#{1,6}\s', line):
                        continue
                    # Add line to excerpt
                    excerpt_lines.append(line)
                    word_count += len(line.split())
                    if word_count >= 30:
                        break
                excerpt_text = ' '.join(' '.join(excerpt_lines).split()[:30]) + '...' if word_count > 30 else ' '.join(excerpt_lines)
                # Convert excerpt from Markdown to HTML
                # excerpt_html = markdown.markdown(
                #     excerpt_text,
                #     extensions=[
                #         'fenced_code',       # Enables fenced code blocks
                #         'codehilite',        # Enables syntax highlighting
                #         'extra',             # Extra Markdown features
                #         'sane_lists',        # Improves list handling
                #         'smarty',            # Converts quotes and dashes to smart quotes and dashes
                #     ],
                #     extension_configs={
                #         'codehilite': {
                #             'guess_lang': False,  # Disable language guessing
                #             'css_class': 'highlight',  # CSS class for styling
                #         },
                #     }
                # )
                excerpt_html = md.render(excerpt_text)
                posts.append({
                    'slug': filename[:-3],
                    'title': post.get('title', 'Untitled'),
                    'date': post.get('date', ''),
                    'excerpt': excerpt_html,
                })
    # Sort posts by date (assuming YYYY-MM-DD format)
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def get_post(slug):
    """Get a post by slug."""
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")
    if not os.path.exists(filepath):
        abort(404)
    with open(filepath, 'r', encoding='utf-8') as f:
        post = frontmatter.load(f)
        # Convert Markdown to HTML with extensions
        # html = markdown.markdown(
        #     post.content,
        #     extensions=[
        #         'fenced_code',       # Enables fenced code blocks
        #         'codehilite',        # Enables syntax highlighting
        #         'toc',               # Generates table of contents
        #         'attr_list',         # Allows attribute lists in Markdown
        #         'tables',            # Enables table syntax
        #         'sane_lists',        # Improves list handling
        #         'smarty',            # Converts quotes and dashes to smart quotes and dashes
        #     ],
        #     extension_configs={
        #         'codehilite': {
        #             'guess_lang': False,  # Disable language guessing
        #             'css_class': 'highlight',  # CSS class for styling
        #         },
        #         'toc': {
        #             'permalink': True,    # Adds permalinks to headings
        #         },
        #     }
        # )
        html = md.render(post.content)
        return {
            'title': post.get('title', 'Untitled'),
            'date': post.get('date', ''),
            'content': html
        }

@app.route('/')
def home():
    posts = get_post_list()
    return render_template('home.html', posts=posts, title="Home", current_year=datetime.now().year)

@app.route('/post/<slug>')
def post_detail(slug):
    post = get_post(slug)
    return render_template('post_detail.html', post=post, title=post['title'], current_year=datetime.now().year)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title="Page Not Found", current_year=datetime.now().year), 404

if __name__ == '__main__':
    app.run(debug=True)
