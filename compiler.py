from lexer import lexer
from parser import parser
from symbol_table import SymbolTable
from retention_table import RetentionTable
from validator import Validator

# Initialize components
lexer = build_lexer()
parser = build_parser()
symbol_table = SymbolTable()
retention_table = RetentionTable()
validator = Validator(symbol_table)

data = '''
x = 10 + 5
y = "Hello"
print(x, y)
'''

# Tokenize
lexer.input(data)
for tok in lexer:
    retention_table.add_token(tok)
    if tok.type == "IDENTIFIER" and tok.value not in symbol_table.symbols:
        symbol_table.add_symbol(tok.value, "variable")

# Parse and validate
parser.parse(data, lexer=lexer)

# Display tables
symbol_table.display()
retention_table.display()

