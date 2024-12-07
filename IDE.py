from tkinter import *
import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import sys

class Group11IDE:
    def __init__(self, root):
        self.root = root
        self.file_path = ''
        self.root.title("Group 11")
        self.create_widgets()
        
       
        

        # Create a button to run the code
        # self.run_button = tk.Button(root, text="Run", command=self.run)
        # self.run_button.pack(side=tk.TOP)

        # Create a button to save the code
        # self.save_button = tk.Button(root, text="Save As", command=self.save_code)
        # self.save_button.pack(side=tk.TOP)

    
     # Create a text area for code input
    def create_widgets(self):
        self.code_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 12))
        self.code_input.pack(expand=True, fill='both')

        self.menub = Menu(self.root)
        self.fileb = Menu(self.menub, tearoff=0)
        self.fileb.add_command(label='Open', command=self.open_file)
        self.fileb.add_command(label='Exit', command=self.root.quit)
        self.fileb.add_command(label='Save As', command=self.save_code)
        self.menub.add_cascade(label='File', menu=self.fileb)

        self.runb = Menu(self.menub, tearoff=0)
        self.runb.add_command(label='Run', command=self.run)
        self.menub.add_cascade(label='Run', menu=self.runb)

        self.output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 10), bg="black", fg="white", height=10)
        self.output_area.pack(expand=True, fill='both')
        self.output_area.config(state=tk.DISABLED)

        self.root.config(menu=self.menub)

    #run function
    def run(self):
        #reads the whole file from the top to end
        code = self.code_input.get('1.0', tk.END)
        #opens a temp file and stores the code
        with open("temp.py", "w") as temp_file:
            temp_file.write(code)

        try:
            #run the compiler file
            result = subprocess.run([sys.executable, "c:\\Users\\Rhumeh\\Desktop\\compiler_project\\compiler.py", "temp.py"], capture_output=True, text=True)
            output = result.stdout
            error = result.stderr
            #an area for the output
            self.output_area.config(state=tk.NORMAL)
            #clears the previous output
            self.output_area.delete('1.0', tk.END)
            if output:
                self.output_area.insert(tk.END, output)
            if error:
                self.output_area.insert(tk.END, f"Error:\n{error}")
            self.output_area.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Execution Error", str(e))
    
    #saves the code
    def save_code(self):
        #uses the asksavefile module to save the file
        #makes the default the file python
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
        #if the file path is a python file then write into the file
        #gets the code from the top to end of the file
        if file_path:
            with open(file_path, 'w') as file:
                code = self.code_input.get('1.0', tk.END)
                file.write(code)

    #function to open a file
    #uses the askopen module which is 
    def open_file(self):
        #use 
        try:
            path = askopenfilename(filetypes=[('Python Files', '*.py')])
            if path:
                with open(path, "r") as file:
                    text = file.read()
                    self.code_input.delete('1.0', END)
                    self.code_input.insert('1.0', text)
                    self.file_path(path)
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"An error occured {e}")

if __name__ == "__main__":
    root = tk.Tk()
    ide = Group11IDE(root)
    root.mainloop()