# Sami Dahoux (c) 2021 copyright, all rights reserved

import re
from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import *
from pygments.lexers.c_cpp import CLexer


class FuncLexer(RegexLexer):

    name = 'Func'
    aliases = ['func']
    filenames = ['*.func', '*.f']

    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    IDENT_SIMPLE = r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\:)'
    IDENT_STRUCT = r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\{)'
    IDENT_DOTED = r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\.)'
    IDENT_PARAM = r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(\()'
    IDENT_ALGEBRA = r'([a-zA-Z_][a-zA-Z0-9_]*)(\s*)(<)'

    BUILTINS = words(('boolean', 'string', 'natural', 'integer',
                      'rational', 'real', 'complex', 'any', 'empty'))

    tokens = {

        'link': [
            (r'\.', Punctuation),
            (IDENT, Name.Namespace),
            (r'\}', Punctuation, '#pop')
        ],

        'boolean': [
            (r'true|false', Name.Builtin)
        ],

        'number': [
            (r'(-)?([0-9]+)\.', Number.Float),
            (r'(-)?([0-9]+)\.([0-9]+)(e(-)?[0-9]+)?', Number.Float),
            (r'(-)?([0-9]+)(e(-)?[0-9]+)', Number.Float),
            (r'(-)?([0-9]+)(//[0-9]+)?', Number.Integer.Long),
        ],

        'string': [
            (r'\\.', String.Escape),
            (r'[^\']', String.Single),
            (r'\'', String, '#pop')
        ],

        'base': [
            (IDENT, Name.Variable),
            (r'\s', Whitespace),
            (r'#.*\n', Comment.Single),
            ('"""', Comment.Multiline, 'comment'),
            (r'([a-zA-Z0-9]*)(\')',
             bygroups(String.Interpol, String.Delimiter), 'string'),
            include('number'),
            include('boolean'),
        ],

        'root': [
            ('define', Keyword, 'quantity'),
            ('block', Keyword, 'block'),
            ('require', Keyword, 'requirement'),
            ('import', Keyword, 'import'),
            ('function', Keyword, 'function'),

            include('base'),
        ],

        'block': [
            (IDENT_STRUCT,
             bygroups(Name.Namespace, Whitespace, Punctuation), '#push'),
            (r'\}', Punctuation, '#pop'),
            include('root'),
        ],

        'quantity': [
            (words(('input', 'output', 'buffer', 'constant')), Keyword),
            (IDENT_SIMPLE,
             bygroups(Name.Property, Whitespace, Punctuation), ('#pop', 'constraint')),
            (IDENT_STRUCT,
             bygroups(Name.Class, Whitespace, Punctuation), ('#pop', 'quantity-structured')),
            include('base'),
        ],
        'quantity-structured': [
            (IDENT_SIMPLE,
             bygroups(Name.Property, Whitespace, Punctuation), 'constraint'),
            (IDENT_STRUCT,
             bygroups(Name.Class, Whitespace, Punctuation), '#push'),
            (r'\}', Punctuation, '#pop'),
            include('base'),
        ],

        'requirement': [
            (words(('on', 'derives', 'specializes', 'refines')), Keyword),
            (IDENT_SIMPLE,
             bygroups(Name.Property, Whitespace, Punctuation), ('#pop', 'constraint')),
            (IDENT, Name.Function),
            include('base'),
        ],

        'import': [
            ('as', Keyword),
            (IDENT_DOTED, bygroups(Name.Namespace, Punctuation)),
            (IDENT, Name.Namespace, '#pop'),
            include('base'),
        ],

        'function': [
            (IDENT_PARAM,
             bygroups(Name.Function, Whitespace, Punctuation), 'function-parameters'),
            (r'\:', Punctuation, ('#pop', 'constraint')),
            include('base'),
        ],
        'function-parameters': [

            (IDENT_SIMPLE,
             bygroups(Name.Variable, Whitespace, Punctuation), 'constraint'),
            (r'\)', Punctuation, '#pop'),
            include('base'),
        ],

        'comment': [
            (r'[^"""\{\@]', Comment.Multiline),
            (r'\{', Punctuation, 'link'),
            (r'\@[^\s]+', Comment.Preproc),
            ('"""', Comment.Multiline, '#pop')
        ],

        'constraint': [
            (IDENT_ALGEBRA,
             bygroups(Name.Variable.Decorator, Whitespace, Punctuation), ('algebra-field', 'algebra-dimension')),
            (r'""', String.Doc, 'semantic'),
            (r'\[\[', Punctuation, 'maths'),
            (r'\{\{', Punctuation, 'algorithm'),
            (r'\(\(', Punctuation, 'enumerated'),
            (r'(<<|>>)', Punctuation, 'interval'),
            (r';', Punctuation, '#pop'),
            (BUILTINS, Name.Builtin),
            (IDENT_PARAM, bygroups(Name.Function, Whitespace, Punctuation)),
            (IDENT, Name.Attribute),
            (r'&&|\|\||\*|\*\*', Operator),
            (r'\)', Punctuation),
            include('base'),
        ],

        'semantic': [
            (r'[^\{\{""]', String.Doc),
            (r'\{', Punctuation, 'link'),
            (r'""', String.Doc, '#pop'),
        ],

        'algebra-dimension': [
            (r',', Punctuation),
            (r'>', Punctuation, '#pop'),
            include('number'),
            include('base'),
        ],
        'algebra-field': [
            (r'\)', Punctuation, '#pop'),
            (BUILTINS, Name.Builtin),
            (r'\(', Punctuation),
            include('base'),
        ],

        'interval': [
            (r'(<<|>>)', Punctuation, '#pop'),
            (r'\:', Punctuation),
            include('number'),
            include('base'),
        ],

        'enumerated': [
            (r'\)\)', Punctuation, '#pop'),
            (r',', Punctuation),
            include('number'),
            include('base'),
        ],

        'algorithm': [
            (r'\}\}', Punctuation, '#pop'),
            include('algorithm-expr'),
            include('base'),
        ],
        'algorithm-expr': [
            (words(('let', 'if', 'else', 'for', 'in')), Keyword),
            (words((';', '(', ')', '.', '{', '}', ',')), Punctuation),
            (r';|\(|\)|\{|\}', Punctuation),
            (words(('>', '=', '<', '!=', '>=', '<=', '+',
             '/', '-', '*', '%', '@', '^')), Operator),
            (IDENT, Name.Variable),
            include('number'),
            include('base'),
        ],

        'maths': [
            include('maths-expr'),
            (r'\]\]', Punctuation, '#pop')
        ],
        'maths-expr': [
            include('base'),
            include('number'),
            (words(('let', 'exists', 'for', 'in')), Keyword),
            (words((';', '(', ')', '.', ',')), Punctuation),
            (words(('>', '=', '<', '!=', '>=', '<=', '+',
             '/', '-', '*', '%', '@', '^')), Operator),
            (IDENT, Name.Variable),
        ],
    }
