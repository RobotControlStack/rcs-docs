import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Robot Control Stack Documentation'
author = 'Khaled Gamal'
release = '0.1'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "github_url": "https://github.com/RobotControlStack/rcs-docs",
    "show_prev_next": False,
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
]
