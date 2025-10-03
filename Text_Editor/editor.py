import tkinter as tk
from tkinter import filedialog,messagebox


def new_file():
    text_area.delete(1.0, tk.END)
    root.title("Untitled - Text Editor")
    
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("All Files", "*.*"),
                                                      ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())
        root.title(f"{file_path} - Text Editor")
    
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("All Files", "*.*"),
                                                        ("Text Documents", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Save File", "File saved successfully!")
        root.title(f"{file_path} - Text Editor")
        
root = tk.Tk()
root.title("Untitled - Text Editor")
root.geometry("800x600")
menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

text=tk.Text(root,wrap=tk.WORD,font=('Arial',12),fg='black',bg='white')
text.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()