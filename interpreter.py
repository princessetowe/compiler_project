import itertools
# import argparse
import sys
from parser import exec_function
#works with iterators
def get_user_input():
    #an endless sequence of
    # user inputs
    for i in itertools.count():
        print(sys.argv)#prints the name of the file
        try:
            yield i, input('grp11in[%d]>>' % i)
        except KeyboardInterrupt:
            break

# def exec_function(user_input):
#     #determines if thr input can be compiled as eval or exec
#     try:
#         node = ast.parse(user_input, mode='exec')
#         code = compile(user_input, '<stdin>', 'eval')
#         return lambda src, globals: exec(code, globals)
#     except SyntaxError:
#         return exec
#     return eval

def exec_user_input(i, user_input, user_globals):
    #evaluates a copy od the user input stored in the user_globals fictionary
    user_globals = user_globals.copy()
    try:
        returnval = exec_function(user_input)(
            user_input, user_globals
            )
    except Exception as e:
        print('%s: %s' % (e.__class__.__name__, e))
    else:
        if returnval is not None:
            print('17out[%d]: %s' %(i, returnval))
    return user_globals

def selected_user_globals(user_globals):
    #defines users which return __ or __
    return(
        (key, user_globals(key))
        for key in sorted(user_globals)
        if not key.startswith('__') or not key.endswith('__')
    )

def save_user_globals(user_globals, path='user_globals.txt'):
    with open(path, 'w') as fd:
        for key, val in selected_user_globals(user_globals):
            fd.write('%s = %s (%s)' % (
                key, val, val.__class__.__name__
                ))
def main():
    user_globals = {}
    save_user_globals(user_globals)
    for i, user_input in get_user_input():
        user_globals = exec_user_input(i, 
        user_input, user_globals)

if __name__ == '__main__':
    main()