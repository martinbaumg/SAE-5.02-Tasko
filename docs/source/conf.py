import os
import sys


sys.path.insert(0, os.path.abspath('../Documentation-database'))

project = 'SAE5.02-Tasko'
copyright = '2023, Martin Baumgaertner - Mikhaïl Karapetyan - Louis Pluviose - Nicolas Wagner - Thomas Strub - Victor Uettwiller'
author = 'Martin Baumgaertner - Mikhaïl Karapetyan - Louis Pluviose - Nicolas Wagner - Thomas Strub - Victor Uettwiller'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
