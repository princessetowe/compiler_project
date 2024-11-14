import ast

def exec_function(user_input):
    # Determines if the input can be compiled as eval or exec
    try:
        node = ast.parse(user_input, mode='exec')
        code = compile(node, '<stdin>', 'exec')
        return lambda src, globals: exec(code, globals)
    except SyntaxError:
        return exec
    return eval
