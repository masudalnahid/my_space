# -*- coding: utf-8 -*-
#
# onepice documentation build configuration file, created by
# sphinx-quickstart on Thu May  4 09:58:38 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
#import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = ['sphinx.ext.autodoc',
     'sphinx.ext.doctest',
     'sphinx.ext.intersphinx',
     'sphinx.ext.todo',
     'sphinx.ext.coverage',
     'sphinx.ext.mathjax',  ###
     'sphinx.ext.ifconfig',
     'sphinx.ext.viewcode',
     'sphinx.ext.githubpages',
     'sphinx.ext.graphviz'   ### graphviz画图插
     ]

# on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
# if on_rtd:
#     extensions = ['sphinx.ext.autodoc',
#          'sphinx.ext.doctest',
#          'sphinx.ext.intersphinx',
#          'sphinx.ext.todo',
#          'sphinx.ext.coverage',
#          'sphinx.ext.mathjax',  ###
#          'sphinx.ext.ifconfig',
#          'sphinx.ext.viewcode',
#          'sphinx.ext.githubpages',
#          'sphinx.ext.graphviz',  ### graphviz画图插
#          ]
# else:
#     extensions = [
#       'sphinx.ext.autodoc',
#       'rst2pdf.pdfbuilder',
#       'sphinx.ext.graphviz',  #graphviz画图插
#     ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'onepice'
copyright = u'2017, Jiangxumin'
author = u'Jiangxumin'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.3.3'
# The full version, including alpha/beta/rc tags.
release = u'1.3.3'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.

#language = "zh"
language = "zh_CN"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
html_static_path = []


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'onepicedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'onepice.tex', u'onepice Documentation',
     u'Jiangxumin', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'onepice', u'onepice Documentation',
     [author], 1)
]


##################################################################
# -- Options for Texinfo output -------------------------------------------
##################################################################

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'onepice', u'onepice Documentation',
     author, 'onepice', 'One line description of project.',
     'Miscellaneous'),
]


##################################################################
# -- Options for Epub output ----------------------------------------------
##################################################################

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']



# Example configuration for intersphinx: refer to the Python standard library.
#intersphinx_mapping = {'https://docs.python.org/': None}
intersphinx_mapping = {}


##################################################################

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    \hypersetup{unicode=true}
    \usepackage{CJKutf8}
    \DeclareUnicodeCharacter{00A0}{\nobreakspace}
    \DeclareUnicodeCharacter{2203}{\ensuremath{\exists}}
    \DeclareUnicodeCharacter{2200}{\ensuremath{\forall}}
    \DeclareUnicodeCharacter{2286}{\ensuremath{\subseteq}}
    \DeclareUnicodeCharacter{2713}{x}
    \DeclareUnicodeCharacter{27FA}{\ensuremath{\Longleftrightarrow}}
    \DeclareUnicodeCharacter{221A}{\ensuremath{\sqrt{}}}
    \DeclareUnicodeCharacter{221B}{\ensuremath{\sqrt[3]{}}}
    \DeclareUnicodeCharacter{2295}{\ensuremath{\oplus}}
    \DeclareUnicodeCharacter{2297}{\ensuremath{\otimes}}
    \begin{CJK}{UTF8}{gbsn}
    \AtEndDocument{\end{CJK}}
    ''',
    }
else:
    latex_elements = {
        'papersize' : 'a4paper',
        'utf8extra' : '',
        'inputenc'  : '',
        'babel'     : r'''\usepackage[english]{babel}''',
        'preamble' : r'''
        \usepackage{ctex}
        ''',
    }


# #######################################################################
# # -- Options for PDF output --------------------------------------------------
# #######################################################################
#   
# # Grouping the document tree into PDF files. List of tuples
# # (source start file, target name, title, author, options).
# #
# # If there is more than one author, separate them with \\.
# # For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
# #
# # The options element is a dictionary that lets you override
# # this config per-document.
# # For example,
# # ('index', u'MyProject', u'My Project', u'Author Name',
# # dict(pdf_compressed = True))
# # would mean that specific document would be compressed
# # regardless of the global pdf_compressed setting.
# 
# pdf_documents = [
#   ('index', u'onpice', u'海贼王', u'hankcs'),
# ]
#   
# # A comma-separated list of custom stylesheets. Example:
# pdf_stylesheets = ['a4','zh_CN']
#   
# # Create a compressed PDF
# # Use True/False or 1/0
# # Example: compressed=True
# #pdf_compressed = False
#   
# # A colon-separated list of folders to search for fonts. Example:
# #pdf_font_path = ['C:\\Windows\\Fonts']
#   
# # Language to be used for hyphenation support
# pdf_language = "zh_CN"
#   
# # Mode for literal blocks wider than the frame. Can be
# # overflow, shrink or truncate
# pdf_fit_mode = "shrink"
#   
# # Section level that forces a break page.
# # For example: 1 means top-level sections start in a new page
# # 0 means disabled
# #pdf_break_level = 0
#   
# # When a section starts in a new page, force it to be 'even', 'odd',
# # or just use 'any'
# #pdf_breakside = 'any'
#   
# # Insert footnotes where they are defined instead of
# # at the end.
# #pdf_inline_footnotes = True
#   
# # verbosity level. 0 1 or 2
# #pdf_verbosity = 0
#   
# # If false, no index is generated.
# #pdf_use_index = True
#   
# # If false, no modindex is generated.
# #pdf_use_modindex = True
#   
# # If false, no coverpage is generated.
# #pdf_use_coverpage = True
#   
# # Documents to append as an appendix to all manuals.
# #pdf_appendices = []
#   
# # Enable experimental feature to split table cells. Use it
# # if you get "DelayedTable too big" errors
# #pdf_splittables = False
#   
# # Set the default DPI for images
# #pdf_default_dpi = 72
#   
# # Enable rst2pdf extension modules (default is only vectorpdf)
# # you need vectorpdf if you want to use sphinx's graphviz support
# #pdf_extensions = ['vectorpdf']
#   
# # Page template name for "regular" pages
# #pdf_page_template = 'cutePage'
#   
# # Show Table Of Contents at the beginning?
# # pdf_use_toc = False
#   
# # How many levels deep should the table of contents be?
# pdf_toc_depth = 2
#   
# # Add section number to section references
# pdf_use_numbered_links = False
#   
# # Background images fitting mode
# pdf_fit_background_mode = 'scale'


#######################################################################
# -- Options for graphviz  seting -------------------------------------
#######################################################################

# 设置 graphviz_dot 路径
graphviz_dot = 'dot'
# 设置 graphviz_dot_args 的参数，这里默认了默认字体
graphviz_dot_args = ['-Gfontname=Georgia', 
                     '-Nfontname=Georgia',
                     '-Efontname=Georgia']
# 输出格式，默认png，这里我用svg矢量图
graphviz_output_format = 'svg'

