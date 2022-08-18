#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created July 2022.

@author: mthansen
"""

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
cwd=os.getcwd()
p=f'{cwd}/../'

import ampyl


# -- Project information -----------------------------------------------------

project = 'ampyl'
copyright = '2022, Maxwell T. Hansen'
author = 'Maxwell T. Hansen'

# The full version, including alpha/beta/rc tags
release = str(ampyl.__version__)

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.githubpages',
    'nbsphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

autosummary_generate = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'press'
html_title = project + ' version ' + release
html_theme = 'jupyter'
html_theme_path = [p+'/doc']
html_theme_options = {
    # 'nosidebar': True,
    # 'sidebarwidth': 300,
    'body_max_width': None,
    'navigation_with_keys': True,
}
#html_sidebars = {
#    '**': [
#        # 'globaltoc.html',
#        'localtoc.html',
#        # 'relations.html',
#        # 'sourcelink.html',
#        'searchbox.html',
#    ]
#}
html_sidebars = {
    '**' : ['localtoc.html','searchbox.html','logo.html']
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# html_theme_options = {
#   "external_links": [
#       ("Github", "https://github.com/mthansen/ampyl"),
#   ]
# }
