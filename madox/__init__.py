import re
from pathlib import Path
from typing import Literal, Mapping, Sequence

from ._version import __version__, version, __version_tuple__, version_tuple


req_extensions = [
    'sphinxcontrib.jquery'
]
static_path = str(Path(__file__).absolute().parent / '_static')


def general(
    templates_path=['_templates'],
    root_doc='index',

    html_static_path=['_static', static_path],
    html_css_files=['style.css'],
    html_js_files=['script.js'],

    napoleon_google_docstring=False,
    todo_include_todos=True,
    trim_footnote_reference_space=True,
):
    return locals()


def intersphinx():
    intersphinx_mapping = {
        'python': ('https://docs.python.org/3/', None),
        'numpy': ('https://numpy.org/doc/stable/', None),
        'astropy': ('https://docs.astropy.org/en/stable/', None),
        'torch': ('https://pytorch.org/docs/stable', None),
        'pyro': ('https://docs.pyro.ai/en/stable/', None),
    }

    return locals()


def autodoc(
    autodoc_inherit_docstrings: bool = False,
    autodoc_class_signature: Literal['mixed', 'separated'] = 'separated',
    autodoc_typehints: Literal['signature', 'description', 'both', 'none'] = 'description',
    autodoc_typehints_description_target: Literal['all', 'documented', 'documented_params'] = 'documented_params',
    autodoc_member_order: Literal['alphabetical', 'groupwise', 'bysource'] = 'groupwise',
    autodoc_mock_imports: list[str] = [],
    autodoc_type_aliases: Mapping[str,  str] = {}
):
    return locals()


def ipython_directive(
    ipython_rgxin=re.compile(r'>>>\s*(?P<line>.*?)\s*$'),
    ipython_promptin: str = '>>>'
):
    return locals()


def nbsphinx(
    nbsphinx_input_prompt='In [%s]:',
    nbsphinx_codecell_lexer='python3'
):
    return locals()


# language=rst
rst_prolog = nbsphinx_prolog = '''
.. default-role:: any
.. highlight:: python3

.. |Python| replace:: Python
.. |pytorch| replace:: `PyTorch`_
.. _pytorch: https://pytorch.org/
.. |Pyro| replace:: `Pyro`_
.. _Pyro: https://pyro.ai
.. |astropy| replace:: `AstroPy`_
.. _astropy: https://www.astropy.org/

.. |citation needed| replace:: `[citation needed]`:superscript:
.. role:: strike
    :class: strike
.. role:: underline
    :class: underline
.. role:: smallcaps
    :class: small-caps

.. role:: arg(literal)

.. role:: raw-html(raw)
    :format: html

.. role:: shell(code)
    :class: highlight
    :language: shell
.. role:: python(code)
    :class: highlight
    :language: python3
.. role:: regex(code)
    :class: highlight
    :language: regex
.. role:: json(code)
    :class: highlight
    :language: json
.. role:: yaml(code)
    :class: highlight
    :language: yaml
'''
