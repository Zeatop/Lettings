import os
import sys
import django

# chemins vers le code source
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../lettings'))
sys.path.insert(0, os.path.abspath('../profiles'))
sys.path.insert(0, os.path.abspath('../oc_lettings_site'))

# Configuration Django pour autodoc
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
django.setup()

project = 'Lettings'
copyright = '2025, Leo Jackson'
author = 'Leo Jackson'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

autodoc_default_options = {
    'members': True,           # Inclure tous les membres
    'member-order': 'bysource',  # Ordre d'apparition dans le code
    'special-members': '__init__',  # Inclure __init__
    'undoc-members': True,     # Inclure les membres sans docstring
    'exclude-members': '__weakref__'  # Exclure __weakref__
}

# Configuration autosummary
autosummary_generate = True
autosummary_imported_members = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False
}
