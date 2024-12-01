from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
import tkinter.scrolledtext as scrolledtext
import subprocess
compiler = tk.Tk()

compiler.title('Group 11')

# def run():
#     command = 'python {file}'
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
#     output, error = process.communicate()
#     code_output.insert('1.0', output)
#     code_output.insert('1.0', error)
#     code = editor.get('1.0', END)
#     # print(code)
    # exec(code)
    
def save_as():
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    if not path.endswith(".py"):
    #if the file is not a python file then make it a python file
        path += ".py"
    with open(path, 'w') as file:
         code = editor.get('1.0', END)
         file.write(code)

def open_file(path):
    try:
        with open(path, "r") as file:
            name = file.read()
            return name
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")

menub = Menu(compiler)

runb = Menu(menub, tearoff=0)
runb.add_command(label='Run', command=runb)
menub.add_cascade(label='Run', menu=runb)
compiler.config(menu=menub)

text_widget = scrolledtext.ScrolledText(compiler, wrap=tk.WORD)
text_widget.pack(expand=True, fill='both')
text_widget.configure(font=("TkDefaultFont", 10))

fileb = Menu(menub, tearoff=0)
fileb.add_command(label='Open', command=open_file)
fileb.add_command(label='Exit', command=exit)
fileb.add_command(label='Save As', command=save_as)
menub.add_cascade(label='File', menu=fileb)
compiler.config(menu=menub)

editor = Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()
compiler.mainloop()