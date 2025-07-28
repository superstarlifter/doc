# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains documentation for StarLifter, a self-service data analysis platform. The documentation is built using Docsify, a documentation site generator that renders Markdown files on the fly.

## Project Structure

- `/docs/` - Contains all documentation markdown files
  - `_sidebar.md` - Navigation structure for the documentation site (controls what appears in the doc navigation)
  - `index.html` - Main entry point for the Docsify site
  - Various markdown files organized in directories:
    - `/getting_started/` - Basic usage guides
    - `/how_to/` - Detailed tutorials and procedures
    - `/analyze/` - Analysis-specific documentation
    - `/internal/` - Internal documentation
- `/docs/assets/` - Contains images and media used in documentation (PNG, JPG, MP4 files)
- `/scripts/` - Contains utility scripts:
  - `generate_flat_docs.py` - Combines all docs into a single markdown file
- `/output/` - Contains generated documentation files

## Common Development Commands

To work with this repository, you'll need:

```bash
# Install Docsify CLI globally (one-time setup)
npm i docsify-cli -g

# Preview the documentation locally on http://localhost:3000
docsify serve docs
```

## Documentation Generation

To generate a combined version of all documentation:

```bash
# Generate a combined markdown file from all documentation
python scripts/generate_flat_docs.py
```

This script:
1. Reads the `_sidebar.md` file to identify all docs
2. Processes each markdown file referenced in the sidebar
3. Converts relative image paths to absolute URLs (https://docs.starlifter.io)
4. Combines all content into a single markdown file in the `output` directory

## Documentation Guidelines

When adding or modifying documentation:
1. Add new pages to the appropriate directory under `/docs/`
2. Update `_sidebar.md` to include navigation links to new pages
3. Place images in `/docs/assets/` and reference them using relative paths
4. Follow the existing markdown formatting patterns

## Key Files

- `/docs/_sidebar.md` - Controls the navigation structure
- `/docs/index.html` - Docsify configuration
- `/docs/css/style.css` - Custom styling for the documentation site

## Documentation Structure

The documentation is organized into three main sections:
1. **Using StarLifter** - Guides for data analysis and visualization
2. **Setting Up StarLifter** - Configuration and data management
3. **Common Uses of StarLifter** - Practical application examples

## GitHub Pages Integration

When changes are committed to this repository, GitHub Pages automatically rebuilds the site using Jekyll, serving the content from the Markdown files. The site is available at https://docs.starlifter.io