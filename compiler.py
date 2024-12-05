from lexer import lexerr, tokens
from parser import Parser
from symboltable import SymbolTable
from validatorr import Validator

def main():
    lexer = lexerr()
    parser = Parser()
    symbol_table = SymbolTable()
    validator = Validator(symbol_table)

    program = '''
    x = 10
    y = 20
    z = x + y
    print(z)
    '''

    print("Tokens:")
    lexer.input(program)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
    # for token in lexer:
    #     print(token)

    print("\nParsing and Execution:")
    try:
        parser.paparse(program)
        print("\nSymbol Table:")
        for name, details in symbol_table.symbols.items():
            print(f"{name}: {details}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()