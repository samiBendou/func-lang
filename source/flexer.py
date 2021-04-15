import re
from pygments.lexer import RegexLexer, bygroups, include, words
from pygments.token import *
from pygments.lexers.c_cpp import CLexer


class FuncLexer(RegexLexer):

    name = 'Func'
    aliases = ['func']
    filenames = ['*.func', '*.f']

    IDENT = r'[a-zA-Z_][a-zA-Z0-9_]*'
    LINK = rf'{{IDENT}}'
    IC = r'#.*\n'
    WS = r'\t|\n| '
    BUILTINS = words(('boolean', 'string', 'natural', 'integer',
                     'rational', 'real', 'complex', 'any', 'empty'))

    tokens = {
        'root': [
            (WS, Escape),

            (IC, Comment.Single),

            (r'"""', Comment.Multiline, 'comment'),

            (rf'({IDENT})?(\')', bygroups(
                String.Affix,
                String.Delimiter),
                'string'),

            (rf'(define)({WS})+(constant)?({WS})*(input|output|buffer)?({WS})*({IDENT})({WS})*(;)',
             bygroups(
                 Keyword,
                 Escape,
                 Keyword,
                 Escape,
                 Keyword,
                 Escape,
                 Name.Class,
                 Escape,
                 Punctuation)),

            (rf'(define)({WS})+(constant)?({WS})*(input|output|buffer)?({WS})*({IDENT})({WS})*(\:)',
             bygroups(
                 Keyword,
                 Escape,
                 Keyword,
                 Escape,
                 Keyword,
                 Escape,
                 Name.Class,
                 Escape,
                 Punctuation),
             'constraint'),

            (rf'(define)({WS})+(constant)?({WS})*(input|output|buffer)?({WS})*({IDENT})({WS})*(\{{)',
             bygroups(
                 Keyword,
                 Escape,
                 Keyword,
                 Escape,
                 Keyword,
                 Escape,
                 Name.Class,
                 Escape,
                 Punctuation),
             'structured'),

            (rf'(block)({WS})+({IDENT})({WS})*',
             bygroups(
                 Keyword,
                 Escape,
                 Name.Namespace,
                 Escape),
             'block'),


            (rf'(import)({WS})+({IDENT})*',
             bygroups(
                 Keyword,
                 Escape,
                 Name.Namespace)),

            (rf'(require)({WS})+({IDENT})({WS})+(on)({WS})+({IDENT})({WS})*(\:)',
             bygroups(
                 Keyword,
                 Escape,
                 Name.Function,
                 Escape,
                 Keyword,
                 Escape,
                 Name.Variable,
                 Escape,
                 Punctuation),
             'constraint'),

            (rf'(function)({WS})+({IDENT})', bygroups(Keyword,
             Escape, Name.Function), 'function'),

            include('number'),
            include('boolean')
        ],

        'function': [
            (rf'\(', Punctuation, 'parameter'),

        ],

        'parameter': [
            (WS, Escape),
            (rf'({IDENT})({WS})*(\:)', bygroups(Name.Variable,
             Escape, Punctuation), 'constraint'),
            (rf'(\))({WS})*(\:)', bygroups(Punctuation,
                                           Escape, Punctuation), ('#pop', 'constraint')),
            (rf'\)', Punctuation, '#pop'),
        ],

        'block': [
            (r'\{', Punctuation, '#push'),
            include('root'),
            (r'\}', Punctuation, '#pop')
        ],

        'comment': [
            (r'[^"""\{\@]', Comment.Multiline),
            (r'\{', Punctuation, 'link'),
            (rf'\@{IDENT}', Comment.Preproc),
            (r'"""', Comment.Multiline, '#pop')
        ],

        'structured': [
            (WS, Escape),
            (r'"""', Comment.Multiline, 'comment'),
            (rf'({IDENT})({WS})*(\:)',
             bygroups(Name.Property, Escape, Punctuation),
             'constraint'),
            (IC, Comment.Single),
            (r'\:', Punctuation, 'constraint'),
            (r'\{', Punctuation),
            (r'\}', Punctuation, '#pop')
        ],

        'constraint': [
            (WS, Escape),
            (BUILTINS, Name.Builtin),
            (rf'({IDENT})(<)', bygroups(
                Name.Variable.Decorator, Punctuation), ('algebraical-field', 'algebraical-dimension')),
            (rf'{IDENT}', Name.Variable.Class),
            (rf'&&|\|\||\*|\*\*', Operator),
            (r'\[\[', Punctuation, 'maths'),
            (r'\{\{', Punctuation, 'algorithm'),
            (r'\(\(', Punctuation, 'enumerated'),
            (r'(<<|>>)', Punctuation, 'interval'),
            (r'""', String.Doc, 'semantic'),
            (r';', Punctuation, '#pop')
        ],

        'algebraical-dimension': [
            (WS, Escape),
            include('number'),
            (r',', Punctuation),
            (r'>', Punctuation, '#pop')
        ],

        'algebraical-field': [
            (BUILTINS, Name.Builtin),
            (r'\(', Punctuation),
            (r'\)', Punctuation, '#pop')
        ],

        'interval': [
            include('number'),
            (r'\:', Punctuation),
            (r'(<<|>>)', Punctuation, '#pop'),
        ],

        'enumerated': [
            (WS, Escape),
            (r',', Punctuation),
            include('number'),
            (rf'({IDENT})?(\')', bygroups(
                String.Affix,
                String.Delimiter),
                'string'),
            (r'\)\)', Punctuation, '#pop')
        ],

        'algorithm': [
            (WS, Escape),
            include('algorithm-expr'),
            (r'\}\}', Punctuation, '#pop')
        ],

        'algorithm-expr': [
            (WS, Escape),
            include('number'),
            (words(('let', 'if', 'else', 'for', 'in')), Keyword),
            (words((';', '(', ')', '.', '{', '}', ',')), Punctuation),
            (r';|\(|\)|\{|\}', Punctuation),
            (rf'({IDENT})', Name.Variable),
            (words(('>','=','<','!=','>=','<=','+','/','-','*','%','@','^')), Operator),
        ],

        'maths': [
            include('maths-expr'),
            (r'\]\]', Punctuation, '#pop')
        ],

        'maths-expr': [
            (WS, Escape),
            include('number'),
            (words(('let', 'exists', 'for', 'in')), Keyword),
            (words((';', '(', ')', '.', ',')), Punctuation),
            (rf'({IDENT})', Name.Variable),
            (words(('>','=','<','!=','>=','<=','+','/','-','*','%','@','^')), Operator),
        ],

        'semantic': [
            (r'[^\{""]', String.Doc),
            (r'\{', Punctuation, 'link'),
            (r'""', String.Doc, '#pop'),
        ],

        'link': [
            (WS, Escape),
            (r'\.', Punctuation),
            (rf'{IDENT}', Name.Variable),
            (r'\}', Punctuation, '#pop')
        ],

        'string': [
            (r'[^\'\n]', String.Delimiter),
            (r'\\.', String.Escape),
            (r'\'', String, '#pop')
        ],

        'boolean': [
            (r'true|false', Name.Builtin)
        ],

        'number': [
            (r'(-)?([0-9]+)\.', Number.Float),
            (r'(-)?([0-9]+)\.([0-9]+)(e(-)?[0-9]+)?', Number.Float),
            (r'(-)?([0-9]+)(e(-)?[0-9]+)', Number.Float),
            (r'(-)?([0-9]+)(//[0-9]+)?', Number.Integer.Long),
        ]
    }
