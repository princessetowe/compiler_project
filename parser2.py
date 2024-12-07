import ply.yacc as yacc
from lexer import * 

#handles precedence
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

#grammar rules
def p_statement(p):
    """statement : expression
                 | assignment
                 | control_structure
                 | function_def
                 | empty"""
    p[0] = p[1]

def p_expression(p):
    """expression : term
                  | expression PLUS term
                  | expression MINUS term"""
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_term(p):
    """term : factor
            | term MULTIPLY factor
            | term DIVIDE factor"""
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_factor(p):
    """ factor : NUMBER
              | STRING
              | IDENTIFIER
              | LPAREN expression RPAREN """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_assignment(p):
    """assignment : IDENTIFIER EQUAL expression"""
    p[0] = ('assign', p[1], p[3])

def p_control_structure(p):
    """control_structure : if_statement
                         | while_loop
                         | for_loop"""
    p[0] = p[1]

def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN statement ELSE statement
                    | IF LPAREN expression RPAREN statement"""
    if len(p) == 6:
        p[0] = ('if', p[3], p[5])
    else:
        p[0] = ('if', p[3], p[5], p[7])

def p_while_loop(p):
    """while_loop : WHILE LPAREN expression RPAREN statement"""
    p[0] = ('while', p[3], p[5])

def p_for_loop(p):
    """for_loop : FOR LPAREN assignment expression RPAREN statement"""
    p[0] = ('for', p[3], p[4], p[6])

def p_function_def(p):
    """function_def : DEF IDENTIFIER LPAREN RPAREN statement"""
    p[0] = ('function', p[2], p[5])

def p_empty(p):
    """empty :"""
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

#calling the yacc and assigning to gthe variable
parser = yacc.yacc()
program = '''
a = 10 
y = 90
return y
'''

lexer.input(program)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok.type, tok.value, tok.lineno, tok.lexpos)


parser.parse(program)
