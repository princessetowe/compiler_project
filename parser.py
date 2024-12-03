import ply.yacc as yacc
from lexer import tokens

class Parser:
    def __init__(self):
        self.parser = yacc.yacc(module=self)

    #function for simple statements
    def stat_expr(self,p):
        '''statement : expression'''
        print("Valid statement:", p[1])

    #function for binary operations
    def binop_expr(self,p):
        '''expression : expression OPERATOR expression'''
        p[0] = (p[2], p[1], p[3])
        #represents it in a tuple p[1] = left operand  p[2] = for the operator p[3]=right operand

    #function for numbers
    def num_expr(self,p):
        '''expression : NUMBER'''
        p[0] = p[1]  #assigns the number

    #function for strings
    def string_expr(self,p):
        '''expression : STRING'''
        p[0] = p[1]  #assigns the string

    #function for identifier(variable names)
    def iden_expr(self,p):
        '''expression : IDENTIFIER'''
        p[0] = p[1]  #assigns the identifier

    #function for syntax error
    def error(self,p):
        if p:
            print(f"Syntax error at '{p.value}' (line {p.lineno})")
        else:
            print("Syntax error at EOF")



