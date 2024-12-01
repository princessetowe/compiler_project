class SymbolTable:
    def __init__(self):
        #an empty dictionary to store symbols
        self.symbol = {}
    
    def add_sym(self, name, type_):
        #adds a symbol to the table if it does not exist
        if name not in self.symbol:
            #stores both the symbol and the type
            self.symbol[name]=type_

    def get_sym(self, name):
        #retrieves the symbol by the name and if it does not exist it returms none
        return self.symbol.get(name, None)
    
    def __repr__(self):
        #returns a string representation of the symbol table for debuhhing
        return f"SymbolTable({self.symbol})"

    def sym_list(self):
        #returns a list of all symbol names
        return list(self.symbols.keys())


   