import ply.lex as lex
#keywords in python
reserved = {
    # 'print' :'PRINT',
    # 'class':'CLASS',
    # 'break':'BREAK',
    'for':'FOR',
    # 'return':'RETURN',
    # 'try':'TRY',
    #'except':'EXCEPT',
    'while':'WHILE',
    'def':'DEF',
    'if':'IF',
    'else':'ELSE',
}
#list of tokens
tokens= ['NUMBER', 'STRING', 'IDENTIFIER', 'LPAREN', 'RPAREN', 
'PLUS','MINUS', 'MULTIPLY', 'DIVIDE', 'EQUAL']+ list(reserved.values())
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MINUS = r'-'
t_PLUS = r'\+'
t_EQUAL = r'\='
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

t_ignore = ' \t\n,'

#function for numbers
def t_NUMBER(t):
    r'\d+'       
    t.value = int(t.value)
    return t

#handles strings
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1] 
    return t

#handles identifiers 
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')#checks for the reserve keywords
    #t.value = (t.value, symbol_lookup(t.value)) # Check if it's a reserved word
    return t

#checks for characters that were not tokenised
def t_error(t):
    print(f"Illegal character '%s'{t.value[0]}'")
    t.lexer.skip(1)

#handles newline
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#handles comments by ignoring them
def t_comment(t):
    r'\#'
    pass

lexer = lex.lex()

# data = '''
# a = 3+4*10
# + -20 *2
# print(a)
# '''
# lexer.input(data)
# while True:
#     tok = lexer.token()
#     if not tok:
#         break
#     print(tok.type, tok.value, tok.lineno, tok.lexpos)