# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.append(os.path.abspath("_themes"))

project = 'Secure Software Development, Security, and Operations (DevSecOps) Practices'
author = 'NIST NCCoE'
googleanalytics_id = 'G-RJSMY46M5C'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.rsvgconverter',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_design',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'nccoe_rtd_theme',
    "sphinxcontrib.mermaid",
    "sphinx_datatables",
    "sphinxcontrib.googleanalytics",
    "sphinx_reredirects",
]

# Redirect legacy documentation URLs to their Example Implementation locations.
redirects = {
    "executive-summary": "example-implementation-1-2/executive-summary.html",
    "introduction": "example-implementation-1-2/introduction.html",
    "notational-reference-model": "example-implementation-1-2/notational-reference-model.html",
    "mapping-ssdf": "example-implementation-1-2/mapping-ssdf.html",
    "example-implementations": "example-implementation-1-2/example-implementations.html",
    "functional-demonstrations": "example-implementation-1-2/functional-demonstrations.html",
    "functional-demonstration-scenarios": "example-implementation-1-2/functional-demonstration-scenarios.html",
    "functional-demonstration-results": "example-implementation-1-2/functional-demonstration-results.html",
    "next-steps": "example-implementation-1-2/next-steps.html",
    "appendix-a": "example-implementation-1-2/appendix-a.html",
    "appendix-b": "example-implementation-1-2/appendix-b.html",
    "appendix-c": "example-implementation-1-2/appendix-c.html",
    "appendix-d": "example-implementation-1-2/appendix-d.html",
    "appendix-e": "example-implementation-1-2/appendix-e.html",
}

# Optionally include the spelling extension only if it's installed
try:
    import sphinxcontrib.spelling
except Exception:
    pass
else:
    extensions.append("sphinxcontrib.spelling")

spelling_word_list_filename = [
    "_themes/nccoe_rtd_theme/dictionaries/spelling_wordlist.txt"
]


templates_path = ['_templates']
source_suffix = '.rst'
gettext_compact = False
exclude_patterns = ['build', 'Thumbs.db', '.DS_Store', '.git']

master_doc = 'index'
suppress_warnings = ['image.nonlocal_uri']
pygments_style = 'default'




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "nccoe_rtd_theme"
html_theme_path = [os.path.abspath("_themes")]
html_static_path = ['_static']
html_theme_options = {
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    'flyout_display': 'hidden',
    'version_selector': False,
    'language_selector': False,
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'project_page': 'https://www.nccoe.nist.gov/projects/secure-software-development-security-and-operations-devsecops-practices'
}
html_css_files = [
    "custom.css"
]

html_js_files = [
    "main.js"
]

numfig = True

email = u'nccoe-devsecops@list.nist.gov'
html_show_sourcelink = True

html_context = {
    "email": u'nccoe-devsecops@list.nist.gov',
    "email_subject": u'[Doc review] {PROJECT} - {N} comments'
}

# Use xelatex for better font/Unicode support
latex_engine = "xelatex"

# (Optional) Set a clean paper size & font size
latex_elements = {
    "papersize": "letterpaper",  # or 'a4paper'
    "pointsize": "11pt",
}