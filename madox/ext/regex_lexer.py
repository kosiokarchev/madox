import re

import pygments.lexers
import sphinx.highlighting
from pygments.lexer import bygroups, RegexLexer
from pygments.token import Comment, Keyword, Name, Number, Operator, Punctuation, String
from sphinx.application import Sphinx


class regexLexer(RegexLexer):
    name = 'regex'

    aliases = 'regex',

    tokens = {
        'root': [
            ('|'.join(map(re.escape, (*r'.*+?|-', '*?', '+?', '??'))), Operator),
            (r'({)(\d+)(?P<second>(,)(\d+))?(})(?(second)\??|)', bygroups(Punctuation, Number, None, Punctuation, Number, Punctuation, Operator)),
            (r'[\$\^]', Name.Builtin),
            ('|'.join(map(re.escape, ('\\'+_ for _ in 'AbBdDsSwWZ'))), Name.Builtin),
            ('\\\\.', String.Escape),
            ('\(\?\#.*?\)', Comment),
            (r'\(\?(?:\:|\=|\!|\<\=|\<\!)', Keyword.Namespace),
            (r'(\(\?P)(\<)([_\w\d][\w\d]*)(\>)', bygroups(Keyword.Namespace, Punctuation, Name.Variable, Punctuation)),
            (r'(\(\?)(\()([_\w\d][\w\d]*)(\))', bygroups(Keyword.Namespace, Punctuation, Name.Variable, Punctuation)),
            (r'(\(\?P)(=)([_\w\d][\w\d]*)', bygroups(Keyword.Namespace, Punctuation, Name.Variable)),
            (r'\(|\)|\[\^?|\]', Keyword.Namespace),
            (r'.', String.Single),
        ],
    }


def setup(app: Sphinx):
    sphinx.highlighting.lexers['regex'] = regexLexer()
    pygments.lexers.LEXERS['regexLexer'] = __name__, regexLexer.name, regexLexer.aliases, None, None
    pygments.lexers._lexer_cache['regex'] = regexLexer
