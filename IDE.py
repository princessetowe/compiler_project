from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
import keyword
import re

class Group11IDE:
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(2)  # Improve DPI awareness on Windows
    except:
        pass
    def __init__(self, root):
        self.result = None
        self.root = root
        self.file_path = ''
        self.root.title("Group 11")
        # self.frame = Frame
        self.create_widgets()

       
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

        # self.frame.pack(expand=True, fill='both')

        # self.l_num = tk.Text(frame, width=4, padx=3, takefocus=0, border=0, background="black", foreground="white", state='disabled', wrap='none')
        # self.l_num.grid (row=0, column=0, rowspan=2, sticky='ns')

        self.root.config(menu=self.menub)

    #run functio
    def run(self):
        #reads the whole file from the top to end
        code = self.code_input.get('1.0', tk.END)
        #opens a temp file and stores the code

        try:
            #run the compiler file
            result = subprocess.Popen(["python", "-c", code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = result.communicate()
            # output = result.stdout
            # error = result.stderr
            #an area for the output
            self.output_area.config(state=tk.NORMAL)
            #clears the previous output
            self.output_area.delete('1.0', tk.END)
            if stdout:
                self.output_area.insert(tk.END, stdout)
            if stderr:
                self.output_area.insert(tk.END, f"Error:\n{stderr}")
            self.output_area.config(state=tk.DISABLED)

        except Exception as e:
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert(tk.END, f"Execution error: {str(e)}", "error")
            self.output_area.config(state=tk.DISABLED)
            #messagebox.showerror("Execution Error", str(e))
    
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


    def highlight_keywords(self, event=None):
        text_widget.tag_remove("keyword", "1.0", tk.END)
        keywords = keyword.kwlist
        for kw in keywords:
            pattern = r'\b' + kw + r'\b'
            for match in re.finditer(pattern, text_widget.get("1.0", tk.END)):
                start = f"1.0+{match.start()}c"
                end = f"1.0+{match.end()}c"
                text_widget.tag_add("keyword", start, end)
                text_widget.tag_configure("keyword",foreground="blue", font=("Courier New", 10, "bold"))

if __name__ == "__main__":
    root = tk.Tk()
    frame = tk.Frame(root) 
    ide = Group11IDE(root)
    root.mainloop()