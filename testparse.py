from lexer import *
from parser import Parser

# Test input
code = """
x = 10
y = x + 20
if y > 10:
    print(y)
else:
    print("Too small")
"""

# Initialize the parser
parser = Parser()

# Parse the input code
try:
    ast = parser.parse(code)
    print("Generated AST:")
    print(ast)
except SyntaxError as e:
    print("Error:", e)