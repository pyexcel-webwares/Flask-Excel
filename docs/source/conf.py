# -*- coding: utf-8 -*-
DESCRIPTION = (
    'A flask extension that provides one application programming interface ' +
    'to read and write data in different excel file formats' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

intersphinx_mapping = {
}
spelling_word_list_filename = 'spelling_wordlist.txt'
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Flask-Excel'
copyright = u'2015-2017 Onni Software Ltd.'
version = '0.0.5'
release = '0.0.6'
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
    ('index', 'Flask-Excel.tex',
     'Flask-Excel Documentation',
     'Onni Software Ltd.', 'manual'),
]
man_pages = [
    ('index', 'Flask-Excel',
     'Flask-Excel Documentation',
     [u'Onni Software Ltd.'], 1)
]
texinfo_documents = [
    ('index', 'Flask-Excel',
     'Flask-Excel Documentation',
     'Onni Software Ltd.', 'Flask-Excel',
     DESCRIPTION,
     'Miscellaneous'),
]
