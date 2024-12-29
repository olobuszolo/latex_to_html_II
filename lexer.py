import ply.lex as lex

# Tokeny
tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
    'SIN', 'COS', 'TAN', 'LOG', 'SQRT', 'FRAC', 'LBRACE', 'RBRACE',
    'INT', 'IINT', 'IIINT', 'SUP', 'VARIABLE',
    'ALPHA', 'BETA', 'GAMMA', 'DELTA', 'PI'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\\cdot'
t_DIVIDE = r'\\div'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SIN = r'\\sin'
t_COS = r'\\cos'
t_TAN = r'\\tan'
t_LOG = r'\\log'
t_SQRT = r'\\sqrt'
t_FRAC = r'\\frac'
t_INT = r'\\int'
t_IINT = r'\\iint'
t_IIINT = r'\\iiint'
t_SUP = r'\^'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_VARIABLE = r'[a-zA-Z]'
t_ALPHA = r'\\alpha'
t_BETA = r'\\beta'
t_GAMMA = r'\\gamma'
t_DELTA = r'\\delta'
t_PI = r'\\pi'

t_ignore = ' \t'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    print(f"Illegal character {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()