# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal academic website built using the al-folio Jekyll theme (https://github.com/alshedivat/al-folio). The site is deployed via GitHub Pages and serves as an academic portfolio for Nick Konz, a PhD candidate at Duke University focused on machine learning and medical image analysis.

## Development Commands

### Local Development
**Docker (Recommended):**
```bash
docker compose pull
docker compose up
```
The site will be available at http://localhost:8080

**Legacy Setup:**
```bash
bundle install
pip install jupyter  # if using Jupyter notebooks
bundle exec jekyll serve --lsi
```

### Building and Deployment
**Build site locally:**
```bash
bundle exec jekyll build --lsi
```

**CSS optimization (removes unused CSS):**
```bash
purgecss -c purgecss.config.js
```

**Manual deployment to GitHub Pages:**
```bash
./bin/deploy
```
Note: Automatic deployment is configured via GitHub Actions on pushes to master.

## Site Architecture

### Key Files and Directories
- `_config.yml` - Main Jekyll configuration with site metadata, theme settings, and plugin configuration
- `_pages/` - Main site pages (about, research, CV, etc.)
- `_projects/` - Project collection files (Markdown)
- `_posts/` - Blog posts (currently contains example posts)
- `_bibliography/papers.bib` - Publications database for automatic bibliography generation
- `_data/` - YAML data files (CV info, coauthors, venues)
- `_layouts/` - HTML templates for different page types
- `_includes/` - Reusable HTML components
- `_sass/` - Sass/SCSS stylesheets
- `assets/` - Static assets (images, PDFs, JavaScript, CSS)

### Content Management
- **Publications**: Managed via BibTeX in `_bibliography/papers.bib`. Jekyll-scholar plugin automatically generates publication pages with buttons, abstracts, and links.
- **News/Announcements**: Add Markdown files to `_news/` directory
- **Projects**: Add Markdown files to `_projects/` directory
- **CV**: Managed via YAML data in `_data/cv.yml` and JSON in `assets/json/resume.json`

### Theme Features
- Responsive design with Bootstrap
- Publication management with BibTeX
- Project galleries with image support
- News/announcements feed
- Social media integration
- Dark/light mode (currently disabled)
- Mathematical notation support via MathJax
- Code syntax highlighting
- Image optimization and WebP conversion

## Jekyll Plugins in Use
- jekyll-scholar (bibliography management)
- jekyll-imagemagick (responsive images)
- jekyll-jupyter-notebook (Jupyter integration)
- jekyll-minifier (asset optimization)
- jekyll-feed (RSS feeds)
- jekyll-sitemap (SEO)
- jekyll-paginate-v2 (pagination)

## Configuration Notes
- Site uses `master` branch for source and `gh-pages` for deployment
- GitHub Actions handles automatic deployment on push to master
- Base URL: https://nickk124.github.io
- The site owner is configured as Nicholas (Nick) Konz with Duke University email
- Google Scholar integration enabled
- Social media profiles configured (GitHub, Twitter, LinkedIn)

## Development Tips
- Always test locally before pushing changes
- Publications automatically generate from BibTeX - edit `papers.bib` for bibliography updates
- Profile image and other assets go in `assets/img/`
- The purgecss.config.js optimizes CSS by removing unused classes - run after major style changes