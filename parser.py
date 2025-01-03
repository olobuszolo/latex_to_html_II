import ply.yacc as yacc
from lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
    ('right', 'SUP')
)


def p_expression_binop(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_binop(p):
    '''term : term TIMES factor
            | term DIVIDE factor'''
    if p[2] == '\\cdot':
        p[2] = '&middot;'
    elif p[2] == '\\div':
        p[2] = '&divide;'
    p[0] = f"{p[1]} {p[2]} {p[3]}"

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = str(p[1])

def p_factor_variable(p):
    'factor : VARIABLE'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = f"({p[2]})"

def p_factor_trig(p):
    '''factor : SIN LPAREN expression RPAREN
              | COS LPAREN expression RPAREN
              | TAN LPAREN expression RPAREN'''
    if p[1] == '\\sin':
        p[0] = f"sin({p[3]})"
    elif p[1] == '\\cos':
        p[0] = f"cos({p[3]})"
    elif p[1] == '\\tan':
        p[0] = f"tan({p[3]})"

def p_factor_log(p):
    'factor : LOG LPAREN expression RPAREN'
    p[0] = f"log({p[3]})"

def p_factor_sqrt(p):
    'factor : SQRT LBRACE expression RBRACE'
    p[0] = f"&radic;({p[3]})"

def p_factor_frac(p):
    'factor : FRAC LBRACE expression RBRACE LBRACE expression RBRACE'
    numerator = p[3]
    denominator = p[6]
    p[0] = (
        f"<span style='display:inline-block; text-align:center; vertical-align:middle;'>"
        f"<span style='display:block; border-bottom:1px solid;'>{numerator}</span>"
        f"<span style='display:block;'>{denominator}</span>"
        f"</span>"
    )

def p_factor_int_simple(p):
    'factor : INT factor'
    p[0] = f"&int; {p[2]}"

def p_factor_int_with_limits(p):
    'factor : INT LBRACE expression RBRACE SUP LBRACE expression RBRACE expression'
    lower_limit = p[3]
    upper_limit = p[7]
    integrand = p[9]
    p[0] = (
        f"<span style='display:inline-block; vertical-align:middle; margin-right:0.5em;'>"
        f"<span style='font-size:larger; vertical-align:middle;'>&int;</span>"
        f"<span style='display:inline-block; text-align:center; position:relative;'>"
        f"<span style='position:absolute; top:-1.2em;'>{upper_limit}</span>"
        f"<span style='position:absolute; bottom:-1.2em;'>{lower_limit}</span>"
        f"</span>"
        f"</span>{integrand}"
    )

def p_factor_iint_with_limits(p):
    'factor : IINT LBRACE expression RBRACE SUP LBRACE expression RBRACE expression'
    lower_limit = p[3]
    upper_limit = p[7]
    integrand = p[9]
    p[0] = (
        f"<span style='display:inline-block; vertical-align:middle; margin-right:0.5em;'>"
        f"<span style='font-size:larger; vertical-align:middle;'>∫∫</span>"
        f"<span style='display:inline-block; text-align:center; position:relative;'>"
        f"<span style='position:absolute; top:-1.2em;'>{upper_limit}</span>"
        f"<span style='position:absolute; bottom:-1.2em;'>{lower_limit}</span>"
        f"</span>"
        f"</span>{integrand}"
    )

def p_factor_iiint_with_limits(p):
    'factor : IIINT LBRACE expression RBRACE SUP LBRACE expression RBRACE expression'
    lower_limit = p[3]
    upper_limit = p[7]
    integrand = p[9]
    p[0] = (
        f"<span style='display:inline-block; vertical-align:middle; margin-right:0.5em;'>"
        f"<span style='font-size:larger; vertical-align:middle;'>∫∫∫</span>"
        f"<span style='display:inline-block; text-align:center; position:relative;'>"
        f"<span style='position:absolute; top:-1.2em;'>{upper_limit}</span>"
        f"<span style='position:absolute; bottom:-1.2em;'>{lower_limit}</span>"
        f"</span>"
        f"</span>{integrand}"
    )

def p_factor_alpha(p):
    'factor : ALPHA'
    p[0] = '&alpha;'

def p_factor_beta(p):
    'factor : BETA'
    p[0] = '&beta;'

def p_factor_gamma(p):
    'factor : GAMMA'
    p[0] = '&gamma;'

def p_factor_delta(p):
    'factor : DELTA'
    p[0] = '&delta;'

def p_factor_pi(p):
    'factor : PI'
    p[0] = '&pi;'

def p_factor_uminus(p):
    'factor : MINUS factor %prec UMINUS'
    p[0] = f"-{p[2]}"

def p_expression_newline(p):
    'expression : expression NEWLINE expression'
    p[0] = f"{p[1]}<br>{p[3]}"

def p_factor_power(p):
    'factor : factor SUP factor'
    p[0] = f"({p[1]}<sup>{p[3]}</sup>)"

def p_error(p):
    print(f"Syntax error at {p.value if p else 'EOF'}")

parser = yacc.yacc()