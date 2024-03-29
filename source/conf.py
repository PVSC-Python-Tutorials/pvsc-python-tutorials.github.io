# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PV Tutorials'
copyright = '2022, PV OSS community'
author = 'PV OSS community'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_title = 'pvlib tutorials'

# disable the useless empty left sidebar
html_sidebars = {
  "**": []
}

html_theme_options = {
    "github_url": "https://github.com/PV-Tutorials/pv-tutorials.github.io",
    "favicons": [
        {"rel": "icon", "sizes": "16x16", "href": "favicon-16x16.png"},
        {"rel": "icon", "sizes": "32x32", "href": "favicon-32x32.png"},
    ],
}