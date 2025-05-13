# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains documentation for StarLifter, a self-service data analysis platform. The documentation is built using Docsify, a documentation site generator that renders Markdown files on the fly.

## Project Structure

- `/docs/` - Contains all documentation markdown files
  - `_sidebar.md` - Navigation structure for the documentation site
  - Various markdown files organized in directories
- `/docs/assets/` - Contains images used in documentation
- `/scripts/` - Contains utility scripts to process documentation

## Common Development Commands

To work with this repository, you'll need:

```bash
# Install Docsify CLI globally (one-time setup)
npm i docsify-cli -g

# Preview the documentation locally
docsify serve docs
```

## Documentation Generation

There's a Python script to generate a flattened version of the documentation:

```bash
# Generate a combined markdown file from all documentation
python scripts/generate_flat_docs.py
```

This script:
1. Reads the sidebar file to identify all docs
2. Processes each markdown file referenced in the sidebar
3. Fixes image paths to use absolute URLs
4. Combines all content into a single markdown file in the `output` directory

## Documentation Structure

The documentation is organized into three main sections:
1. Using StarLifter - Guides for data analysis and visualization
2. Setting Up StarLifter - Configuration and data management
3. Common Uses of StarLifter - Practical application examples

## GitHub Pages Integration

When changes are committed to this repository, GitHub Pages automatically rebuilds the site using Jekyll, serving the content from the Markdown files.