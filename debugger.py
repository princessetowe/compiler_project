class Debugger:
    def __init__(self):
        self.breakpoints = set()  # Set to store breakpoints
        self.current_line = 0     # Current line of execution
        self.locals = {}          # Dictionary to store local variables

    def set_breakpoint(self, line_number):
        #Set a breakpoint at the specified line number
        self.breakpoints.add(line_number)

    def clear_breakpoint(self, line_number):
        #Clear a breakpoint at the specified line number
        self.breakpoints.discard(line_number)

    def run(self, code):
        #Run the provided code with debugging support
        self.current_line = 0
        self.locals = {}
        code_lines = code.splitlines()

        while self.current_line < len(code_lines):
            if self.current_line + 1 in self.breakpoints:
                print(f"Breakpoint hit at line {self.current_line + 1}: {code_lines[self.current_line]}")
                input("Press Enter to continue...")  # Wait for user to continue

            line = code_lines[self.current_line]
            self.execute_line(line)
            self.current_line += 1

    def execute_line(self, line):
        #execute a single line of code
        try:
            exec(line, {}, self.locals)  #execute the line in the local context
        except Exception as e:
            print(f"Error executing line {self.current_line + 1}: {e}")

    def inspect_locals(self):
        local_vars = self.get_current_locals()
        if local_vars:
            local_vars_str = "\n".join(f"{k}: {v}" for k, v in local_vars.items())
            print("Current local variables:")
            print(local_vars_str)
            return local_vars_str
        return "No local variables found."