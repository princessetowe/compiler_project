import ply.lex as lex
#from token import TokenType, Token

#toekn types
tokens = (
    'NUMBER',
    'STRING',
    'IDENTIFIER',
    'KEYWORD',
    'OPERATOR',
    'COMMENT'
)

#Ignores white spaces and new kine
tok_ignore = '\t\n'
#regular expressions for operators and comments
tok_OPERATOR = r'[+\-*/()=,<>!]'
tok_COMMENT = r'\#.*'

#dictionary of keywords and their token types
keywords = {
    #change this regular expressions
    "print": 'PRINT',
    "def": 'DEF',
    "class": 'CLASS',
    "if":'IF',
    "else":'ELSE',
    "for":'FOR',
    "while":'WHILE',
    "break":'BREAK',
    "return":'RETURN',
    "try":'TRY',
    "except":'EXCEPT'
}

#add keywords to token list
tokens += tuple(keywords.values())
#  "try":TokenType.TRY,
# class Lexer:
#     def __init__(a, text):
#         a.text = iter(text) #gets an iterator from the text object
#         a.advance()#uses the advance funvtion created

    #store characters in a function and users the next function in python
    # def advance(a):
    #     try:
    #         a.current_char = next(a.text) #the next function triggers the iterator next method
    #     except StopIteration:
    #         a.current_char = None #if tehre is no charaacter left thrn end the iterator

    #a function to generate tokens from the text input
    # def generate_token(a):
    #     while a.current_char != None:
    #         if a.current_char in WHITESPACE:
    #             #if it is a whitespace skip 
    #             a.advance()
    #         elif a.current_char in COMMENTS:
    #             #skips comments
    #             a.advance()
    #         elif a.current_char in TEXTS:
    #             #uses the generate text function
    #             yield a.generate_keyword()
    #         elif a.current_char in STRING:
    #             yield a.generate_string()
    #         elif a.current_char == '.'   or a.current_char in DIGITS:
    #             a.generate_number()
    #         elif a.current_char in EQUALS:
    #             a.advance()
    #         elif a.current_char in ('+', '-', '*', '/', '(', ')', ',', '=', '<', '>', '!'):
    #             yield Token(type=TokenType.OPERATOR, value=a.current_char)
    #             a.advance()
    #         else:
    #             raise ValueError(f"Unexpected character: {a.current_char}")

#setting tokens to numbers  
def tok_number(a):
    r'\d+(\. \d*)?'
    try:
        a.value = int(a.value)
    except ValueError:
        a.value = float(a.value)
    a.type = "NUMBER"
    return a
    # decimal_point_count = 0
    # num_str = a.current_char
    # a.advance()

        # while a.current_char !=  None and (a.current_char == '.' or a.current_char in DIGITS):
        #     if a.current_char == '.':
        #         decimal_point_count += 1
        #         if decimal_point_count > 1:
        #             break
        #     num_str += a.current_char
        #     a.advance()

        # if num_str.startswith('.'):
        #     num_str = '0' + num_str
        # if num_str.endswith('.'):
        #     num_str = '0' + num_str

        # return Token(TokenType.NUMBER, float(num_str))

 #sets token type to string       
def tok_STRING(a):
    r'"([^"\\]|\\.)*"'
    a.value = a.value[1:-1]#removes the quote
    return a

#for variables, functions or class names
def tok_IDENTIFIER(a):
    r'[a-zA-Z_]\w*'#checks for characters
    if a.value not in keywords:#checks if it is keyword
        return a
    else:
        pass

#for comments
def tok_COMMENT(a):
    r'\#.*'#checks for single comments
    pass#ignores comments

#handles illegal char
def tok_error(a):
    print(f"Illegal character '{a.value[0]}'")#prints the char
    a.lexer.skip(1)#skips char

def lexerr():
    lexer = lex.lex()


data = '''
print("Hello, world!")
x = 10 + 5
y = "This is a string"
# This is a comment
'''

lexer.input(data)

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    # def generate_keyword(a):
    #     key_str = a.current_char
    #     a.advance()
    #     while a.current_char != None and (a.current_char in LETTERS +DIGITS + '_'):
    #         key_str += a.current_char
    #         a.advance()
    #     tt = KEYWORDS.get(identifier, TokenType.IDENTIFIER)
    #     return  Token(type=TokenType.STRING, value=string)

    # def generate_string(a):
    #     string = ''
    #     #skip the quote
    #     a.advance()
    #     while a.current_char is not None and a.current_char != STRING:
    #         string += a.current_char
    #         a.advance()
    #         if a.current_char is None:
    #             raise ValueError ("Terminate the string")
    #             a.advance()
    #             return Token(type=TokenType.STRING, value=string)