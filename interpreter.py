class Interpreter:
    def __init__(self, asts):
        #assigns the list of asts passed as an argument to the class instance variable
        self.asts = asts
        #used for storing variables or values during the execution of the ast
        self.storage = {}

    def execute(self):
        #iterates over each ast in the list 
        for ast in self.asts:
            #calls the read method of the current ast being iterated and passes the self instance of the interpreter
            ast.read(self)
