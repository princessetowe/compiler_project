from symbol_table import SymbolTable

class Validator:
    def __init__(self, symbol_table):
        self.symbol_table = symbol_table

    def validate_declaration(self, name):
        if name not in self.symbol_table.symbols:
            raise Exception(f"Variable '{name}' not declared.")

    def validate_assignment(self, name, value):
        self.symbol_table.add_symbol(name, type(value).__name__, value)

    def validate_expression(self, name, expected_type):
        symbol = self.symbol_table.get_symbol(name)
        if not symbol or symbol["type"] != expected_type:
            raise Exception(f"Type mismatch for '{name}'. Expected {expected_type}.")
