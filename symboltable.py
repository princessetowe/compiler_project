class SymbolTable:
    def __init__(self):
        self.table = {}

    def add(self, name, symtype, scope):
        if name in self.table:
            raise Exception(f"Symbol {name} already declared in scope{scope}")
        self.table[name] = {"type": symtype,"scope": scope}
    def  check(self, name):
        return self.table.get(name)
    def __repr__(self):
        return "\n".join(f"{key} : {value}")