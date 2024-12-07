from lexer import *
from parser import *
from interpreter import *
from validator import Validator
from debugger import Debugger
from symboltable import SymbolTable
import sys


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

def main():
    print(f"{sys.argv}> ")
    if len(sys.argv) < 2:
        sys.exit(1)

    filename = sys.argv[1]
    data = read_file(filename)

    debugger = Debugger()
    validator = Validator(SymbolTable)

    print("\nParsing and Execution:")
    try:
        debugger.set_breakpoint(3)
        debugger.run(data)
        parse_d(data)
        
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()