# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: 2022 Sidings Media <contact@sidingsmedia.com>
# SPDX-License-Identifier: CC0-1.0

import subprocess

# -- Project information -----------------------------------------------------

project = 'Developer Documentation - Railway Controller'
copyright = '2022, Sidings Media'
author = 'Sidings Media'

# Versions
# These may get over written later depending upon the branch and tags.
# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''
warning = ''

revision = subprocess.check_output(
    ['git', 'rev-parse', '--short', 'HEAD']).strip().decode('ascii')
out = subprocess.check_output(["git", "branch"]).decode("utf8")
current = next(line for line in out.split("\n") if line.startswith("*"))
branch = current.strip("*").strip()
# Fix where branch output is (HEAD DETACHED AT ORIGIN/
if branch[0] == '(':
    branch = branch[25:-1]

if branch == 'develop':
    version = f'DEV-{revision}'
    release = f'DEV-{revision}'
    warning = 'This documentation is a development version and as such it is unstable and is prone to change at any time.'
    revisionNotice = f"Revision {revision} on branch {branch}"
elif branch == "main":
    version = revision
    release = revision
    warning = ""
    revisionNotice = f"Revision {revision} on branch {branch}"
else:
    # Try to get the current tag
    try:
        tag = subprocess.check_output(
            ['git', 'describe', '--tags', '--abbrev=0', '--exact-match']).strip().decode('ascii')
    except subprocess.CalledProcessError:
        tag = None
    if tag is None:
        revisionNotice = f"Revision {revision} on branch {branch}"
        if version == '':
            version = f"{branch.upper()}-{revision}"
        if release == '':
            release = f"{branch.upper()}-{revision}"
    
    else:
        # The short X.Y version
        version = tag
        # The full version, including alpha/beta/rc tags
        release = tag
        warning = ''
        revisionNotice = f"Revision {revision} on tag {tag}"

# -- General configuration ---------------------------------------------------


extensions = [
    "sphinxcontrib.bibtex",
    "sphinx.ext.autosectionlabel",
    "sphinxcontrib.openapi",
    "sphinxcontrib.redoc"
]
templates_path = ['_templates']
source_suffix = ['.rst']
master_doc = 'index'
language = "en"
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = None
autosectionlabel_prefix_document = True
numfig = True

redoc = [
    {
        'name': 'Railway Controller Client Bridge API',
        'page': 'api/clientbridge',
        'spec': 'specifications/commands/openapi.yaml',
        'embed': True,
    },
]


# -- Options for HTML output -------------------------------------------------
html_theme = "furo"
html_static_path = ['_static']
html_css_files = ["css/rtd-version.css"]
html_js_files = ["js/commithash.js"]
html_title = "Railway Controller"

#html_js_files = [ ]
#html_logo = '_static/track-bw-square-192.png'
#html_favicon = '_static/favicon.ico'

# -- Options for HTMLHelp output ---------------------------------------------

htmlhelp_basename = 'railwaycontrollerdev'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': f'''
        %% --------------------------------------------------
        %% |:sec:| add list of figures, list of tables, list of code blocks to TOC
        %% --------------------------------------------------
        \\makeatletter
        \\renewcommand{{\sphinxtableofcontents}}{{%
        %
        % before resetting page counter, let's do the right thing.
        \\if@openright\\cleardoublepage\\else\\clearpage\\fi
        \\pagenumbering{{roman}}%
        \\begingroup
            \\parskip \\z@skip
            \\tableofcontents
        \\endgroup
        %
        %% addtional lists
        \\if@openright\\cleardoublepage\\else\\clearpage\\fi
        \\addcontentsline{{toc}}{{chapter}}{{List of Figures}}%
        \\listoffigures
        %
        \\if@openright\\cleardoublepage\\else\\clearpage\\fi
        \\addcontentsline{{toc}}{{chapter}}{{List of Tables}}%
        \\listoftables
        %
        \\if@openright\\cleardoublepage\\else\\clearpage\\fi
        \\addcontentsline{{toc}}{{chapter}}{{List of Code Blocks}}%
        \\listof{{literalblock}}{{List of Code Blocks}}%
        %
        \\if@openright\\cleardoublepage\\else\\clearpage\\fi
        \\pagenumbering{{arabic}}%
        }}
        \\makeatother

        % \\addto\\captionsenglish{{\\renewcommand{{\\chaptername}}{{Chapter}}}}
		%%%% Custom copyright
		\\fancyfoot[LO,RE]{{Copyright \\textcopyright\\ 2022, Sidings Media. Licensed under CC-BY-SA-4.0}}
		\\fancypagestyle{{plain}}{{
		\\fancyhf{{}}
		\\fancyfoot[LE,RO]{{\\thepage}}
		\\renewcommand{{\\headrulewidth}}{{0pt}}
		\\renewcommand{{\\footrulewidth}}{{0.4pt}}
		% add copyright stuff for example at left of footer on odd pages,
		% which is the case for chapter opening page by default
        \\fancyfoot[LO,RE]{{Copyright \\textcopyright\\ 2022, Sidings
        Media. Licensed under CC-BY-SA-4.0\\\\{revisionNotice}}}}}
    ''',
    'maketitle': f'''
	\\newcommand\\sphinxbackoftitlepage{{{{This work is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.\\\\\\\\{warning}}}}}\\sphinxmaketitle
	'''
}

latex_show_urls = 'footnote'
latex_documents = [
    (master_doc, 'railwaycontroller.tex', 'Railway Controller',
     'Sidings Media', 'manual'),
]


# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'railwaycontrollerdev', 'Developer Documentation - Railway Controller',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'railwaycontrollerdev', 'Developer Documentation - Railway Controller',
     author, 'SidingsMedia', 'Documentation relating to the Railway Controller project',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']