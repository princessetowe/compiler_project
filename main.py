from tkinter import *
from tkinter.filedialog import asksaveasfilename
import subprocess
compiler = Tk()

compiler.title('Group 11')

def run():
    command = 'python {file}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)
    code = editor.get('1.0', END)
    # print(code)
    # exec(code)
    
def save_as():
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'w') as file:
         code = editor.get('1.0', END)
         file.write(code)
    
menub = Menu(compiler)

runb = Menu(menub, tearoff=0)
runb.add_command(label='Run', command=run)
menub.add_cascade(label='Run', menu=runb)
compiler.config(menu=menub)

fileb = Menu(menub, tearoff=0)
fileb.add_command(label='Open', command=run)
fileb.add_command(label='Exit', command=exit)
fileb.add_command(label='Save As', command=save_as)
menub.add_cascade(label='File', menu=fileb)
compiler.config(menu=menub)

editor = Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()
compiler.mainloop()