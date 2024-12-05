class SymbolTable:
    def __init__(self):
        self.symbol = {}  
    
     #function for adding a symbol to the table if it is not there
    def add(self, name, type_):
        if name not in self.symbol:
            self.symbol[name] = type_  #the type_ is for the symbol type (integer, string e.t.c)
            #for storing in the symbol name and value

    #for getting the type of the symbol by the name    
    def get(self, name):
        #it returns none if it does not exist
        return self.symbol.get(name, None)
    
    def __repr__(self):
        # Returns a string representation of the symbol table for debugging.
        return f"SymbolTable({self.symbol})"

    #function for returning all the symbols by their names
    def list_symbols(self):
        return list(self.symbol.keys())
