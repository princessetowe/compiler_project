from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename, askopenfilename
import tkinter.scrolledtext as scrolledtext
import subprocess
compiler = tk.Tk()

compiler.title('Group 11')

#storing the file path
file_path = ''

#function that captures the file path
def set_file_path(path):
    global file_path
    file_path = path  

def save_as():
    path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    if not path.endswith(".py"):
    #if the file is not a python file then make it a python file
        path += ".py"
    with open(path, 'w') as file:
         code = text_widget.get('1.0', END)
         file.write(code)
         set_file_path(path)

def open_file():
    try:
        path = askopenfilename(filetypes=[('Python Files', '*.py')])
        if path:
            with open(path, "r") as file:
                text = file.read()
                text_widget.delete('1.0', END)
                text_widget.insert('1.0', text)
                set_file_path(path)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        # print(f"{e}")
        print(f"An error occured {e}")

def run():
    code = text_widget.get('1.0', END)
    try:
        with open("temp.py", "w") as main:
            main.write(code)
            process = subprocess.Popen(["python", "compiler.py", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            code_output.config(state=NORMAL)
            code_output.delete('1.0', END)
        
        if error:
            code_output.insert('1.0', error)
            code_output.insert(state=DISABLED)

    except Exception as e:
        code_output.config(state=NORMAL)
        code_output.delete("1.0", END)
        code_output.insert(END, f"Error: {str(e)}", error)
        code_output.config(state=DISABLED)
    # print(code)

def copy_text():
    compiler.clipboard_clear()
    content = text_widget.selection_get()
    compiler.clipboard_append(content)

def paste_text():
    text_widget.insert(INSERT, compiler.clipboard_get())

menub = Menu(compiler)

fileb = Menu(menub, tearoff=0)
fileb.add_command(label='Open', command=open_file)
fileb.add_command(label='Exit', command=exit)
fileb.add_command(label='Save As', command=save_as)
menub.add_cascade(label='File', menu=fileb)

runb = Menu(menub, tearoff=0)
runb.add_command(label='Run', command=run)
menub.add_cascade(label='Run', menu=runb)


compiler.config(menu=menub)

text_widget = Text(compiler, wrap=tk.WORD, font=("Consolas", 12), bg="white", fg="black")
text_widget.pack(expand=True, fill='both')
# text_widget.configure(font=("TkDefaultFont", 10))

text_label = Label(compiler, text="Terminal Output:", font=("Arial", 12))
text_label.pack()

code_output = scrolledtext.ScrolledText(bg="Black", fg='white', height=10, font=("Consolas", 10))
code_output.pack(expand=True, fill='both')
code_output.tag_configure("error", foreground="red")
code_output.config(state=DISABLED)

compiler.mainloop()