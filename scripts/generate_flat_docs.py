import os
import re
from pathlib import Path

BASE_URL = "https://docs.starlifter.io"
DOCS_DIR = "docs"

def fix_image_urls(content):
    """Convert relative image URLs to absolute ones"""
    def replace_markdown_url(match):
        alt_text = match.group(1)
        url = match.group(2)
        # Strip any leading slashes
        url = url.lstrip('/')
        # Replace '../' with base URL
        if url.startswith('..'):
            url = url.replace('..', BASE_URL)
        else:
            url = f"{BASE_URL}/{url}"
        return f'![{alt_text}]({url})'
    
    def replace_html_url(match):
        prefix = match.group(1)
        url = match.group(2)
        suffix = match.group(3)
        # Strip any leading slashes
        url = url.lstrip('/')
        # Replace '../' with base URL
        if url.startswith('..'):
            url = url.replace('..', BASE_URL)
        else:
            url = f"{BASE_URL}/{url}"
        return f'{prefix}{url}{suffix}'
    
    # Fix markdown image syntax
    content = re.sub(r'!\[(.*?)\]\((.*?)\)', replace_markdown_url, content)
    # Fix HTML img tags
    content = re.sub(r'(<img\s+src=")([^"]+)(.*?>)', replace_html_url, content)
    return content

def extract_markdown_links(content):
    """Extract markdown links from content"""
    return re.findall(r'\[(.*?)\]\((.*?\.md)\)', content)

def read_markdown_file(filepath):
    """Read and process a markdown file"""
    try:
        with open(os.path.join(DOCS_DIR, filepath), 'r', encoding='utf-8') as f:
            content = f.read()
        # Add absolute documentation link at the start
        absolute_link = f"{BASE_URL}/#/{filepath}"
        content = f"[View this page on docs.starlifter.io]({absolute_link})\n\n{content}"
        return fix_image_urls(content)
    except FileNotFoundError:
        print(f"Warning: Could not find file {filepath}")
        return f"\n\nMissing content for {filepath}\n\n"

def main():
    # Read sidebar file
    with open(os.path.join(DOCS_DIR, '_sidebar.md'), 'r', encoding='utf-8') as f:
        sidebar_content = f.read()

    # Extract all markdown links
    links = extract_markdown_links(sidebar_content)
    
    # Create output directory if it doesn't exist
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Combine all content
    combined_content = "# StarLifter Documentation\n\n"
    processed_files = set()
    
    for title, filepath in links:
        if filepath not in processed_files:
            combined_content += f"\n## {title}\n\n"
            combined_content += read_markdown_file(filepath)
            processed_files.add(filepath)
    
    # Write combined content
    with open(os.path.join(output_dir, 'combined_docs.md'), 'w', encoding='utf-8') as f:
        f.write(combined_content)

if __name__ == "__main__":
    main()
