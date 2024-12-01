import ply.yacc as yacc
from lexer import tokens

class Parser:
    def __init__(self):
        self.parser = yacc.yacc(module=self)

    # Grammar rule 
    def simple_statement(self,a):
        '''statement : expression'''#handles a simple statement
        print("Valid statement:", a[1])

    #rule for binary expression
    def binop_expr(self,a):
        '''expression : expression OPERATOR expression'''#add, sub, div and mu
        a[0] = (a[2], a[1], a[3])# represents the binary operation as a tuple
    #2= operator, 1 = left operand and 3 = right operand

    #for numbers
    def number_expr(self,a):
        '''expression : NUMBER'''
        a[0] = a[1]

    #for strings
    def string_expr(self,a):
        '''expression : STRING'''
        a[0] = a[1]

    #for ids
    def id_expr(self,a):
        '''expression : IDENTIFIER'''
        a[0] = a[1]

    #for syntax error
    def errorr(self,a):
        print("Syntax error in input!")

    # Build the parser
    def parserr():
        return yacc.yacc()

    # Test the parser
if __name__ == "__main__":
    from lexer import build_lexer
    lexer = build_lexer()
    parser = build_parser()

    data = '''
    x = 10 + 5
    print("Result:", x)
    '''
    parser.parse(data, lexer=lexer)
