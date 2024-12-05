import ply.lex as lex

tokens = (
    'NUMBER',     
    'STRING', 
    'IDENTIFIER',
    'OPERATOR',
    'COMMENT'
)

t_ignore = ' \t\n'
#regular expressions for operators and comments.
t_OPERATOR = r'[+\-*/()=,<>!]' 
t_COMMENT = r'\#.*'            


keywords = {
        "print": 'PRINT',
        "def": 'DEF',
        "class": 'CLASS',
        "if": 'IF',
        "else": 'ELSE',
        "for": 'FOR',
        "while": 'WHILE',
        "break": 'BREAK',
        "return": 'RETURN',
        "try": 'TRY',
        "except": 'EXCEPT'
}
#add keyword tokens to the token list
tokens += tuple(keywords.values())

#function for numbers
def t_NUMBER(t):
    r'\d+(\.\d*)?'
    t.value = int(t.value) if '.' not in t.value else float(t.value)
    return t

    # try:
    #     t.value = int(t.value)  #convert to integer
    # except ValueError:
    #     t.value = float(t.value)  #if it does not convert to an integer then convert to a floating number
    # t.type = "NUMBER"  #set the token type to NUMBER
    # return t

#function for strings
def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1] 
    #removes the quotes
    return t

#function for identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_]\w*'
    t.type = keywords.get(t.value, 'IDENTIFIER')  # Check if it's a reserved word
    return t
    # if t.value not in keywords:  
    #     #checks if it is a keyword
    #     return t

#function for comments
# def tok_COMMENT(t):
#     r'\#.*'
#     pass  #ignores comments

#function for handling errors
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)#skips the illegal character

#function for the lexer
def lexerr():
   return lex.lex()
    
if __name__ == "__main__":
    lexer = lexerr()

    if lexer is None:
        print("Lexer creation failed!")
    else:
        print("Lexer created successfully.")

    data = '''
    print("Hello, world!")
    x = 10 + 5
    y = "This is a string"
    # This is a comment
    '''
    
    lexer.input(data)
    print("tokens:")
    while True:
        tok = lexer.token()
        if not tok:  
            break
        print(tok)
