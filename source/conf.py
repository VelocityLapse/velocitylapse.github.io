# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Velocity Lapse'
copyright = '2025, Noah Rahm'
author = 'Noah Rahm'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'rst2pdf.pdfbuilder',
]

templates_path = ['_templates']
exclude_patterns = []
html_extra_path = ['extras']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
html_favicon = '_static/favicon.png'
html_title = 'Velocity Lapse'
html_logo = '_static/icon.png'
html_static_path = ['_static']
html_css_files = ['custom.css']


# rst2pdf.pdfbuilder

# (source start file, target name, title, author, options).
pdf_documents = [
    ('index', 'Velocity-Lapse-User-Guide', 'Velocity Lapse User Guide', 'Noah Rahm'),
]

# A list of folders to search for stylesheets. Example:
pdf_style_path = ['.', '_static']

# Label to use as a prefix for the subtitle on the cover page
subtitle_prefix = ''

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
pdf_fit_mode = "shrink"

# Background images fitting mode
pdf_fit_background_mode = 'scale'