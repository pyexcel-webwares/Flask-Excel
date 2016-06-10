# -*- coding: utf-8 -*-
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
    'pyexcel': ('http://pyexcel.readthedocs.org/en/latest/', None)
}

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Flask-Excel'
copyright = u'2015-2016 Onni Software Ltd.'
version = '0.0.5'
release = '0.0.5'
exclude_patterns = []
pygments_style = 'sphinx'
import sys  # noqa
import os  # noqa
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ['_themes']
html_theme = 'flask_small'
html_static_path = ['_static']
htmlhelp_basename = 'Flask-Exceldoc'
latex_elements = {}
latex_documents = [
    ('index', 'Flask-Excel.tex', u'Flask-Excel Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'Flask-Excel', u'Flask-Excel Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'Flask-Excel', u'Flask-Excel Documentation',
     'Onni Software Ltd.', 'Flask-Excel', 'One line description of project.',
     'Miscellaneous'),
]
