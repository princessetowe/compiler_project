from symboltable import SymbolTable

class Validator:
    def __init__(self, symbol_table):
        #stores the reference to the symbol table
        self.symbol_table = symbol_table

    def validate_declaration(self, name):
        #checks if the variable exists in the symbol table
        if name not in self.symbol_table.symbols:
            raise Exception(f"Variable '{name}' not declared.")
            #raise an error if it is not found

    def validate_assignment(self, name, value):
        self.symbol_table.add_symbol(name, type(value).__name__, value)
        #add variable to the symbol table

    def validate_expression(self, name, expected_type):
        #retrieves the variable 
        symbol = self.symbol_table.get_symbol(name)
        #check if the variable exists
        if not symbol or symbol["type"] != expected_type:
            raise Exception(f"Type mismatch for '{name}'. Expected {expected_type}.")