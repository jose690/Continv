import tkinter as tk # all lowercase tkinter for Python 3.x


root = tk.Tk()
root.geometry("1280x600")
def write_text():
    print("hello") # Python 3.x requires brackets for print statements.

def command():
    window = tk.Toplevel(root)
    tk.Button(window,text="Button2",command=write_text).grid()
    tk.Label(window,text="hello").grid()

button = tk.Button(root, text="New Window", command=command)
button.grid()

root.mainloop()