# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
sys.path.insert(0, os.path.abspath("../../") )

import maliang

project = 'maliang'
copyright = '2023, 1258843771@qq.com'
author = '1258843771@qq.com'
# release = '0.0.1'
release = maliang.__version__
version = maliang.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autodoc',
]
# autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'classic'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Enable support for both Restructured Text and Markdown
source_suffix = [".rst", ".md"]