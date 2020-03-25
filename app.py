from tkinter import *
import tkinter as tk
import pyperclip


w = tk.Tk()
w.title("Simple Counter")
header = tk.Label(
    text="Simple Counter",
    font=("Courier", 50)
)
w.iconbitmap('icon.ico')
header.pack()

def decrease():
    value = int(res["text"])
    res["text"] = f"{value - 1}"

sub = tk.Button(
    text="-",
    font=("Arial", 60),
    height=3,
    width=4,
    command=decrease
)
sub.pack(side="left")

res = tk.Label(
    text=0,
    font=("Arial", 60),
    height=3,
    width=4
)
res.pack(side="left")

def increase():
    value = int(res["text"])
    res["text"] = f"{value + 1}"



def reset():
    value = int(res["text"])
    res["text"] = (value == 0)

def copy():
    tex = int(res["text"])
    pyperclip.copy(tex)



def popup():
    popup = tk.Tk()
    popup.title("About Simple Counter")
    # geometry is width, height
    popup.geometry("600x300")
    label1 = tk.Label(popup,
                      text="Simple Counter is a free tool \n used to count or keep track of objects",
                      font=("Helvetica", 20, "bold"))
    label1.pack(pady=10)
    label2 = tk.Label(popup, text="Version 1.0.1", font=("Helvetica", 10, "bold"))
    label2.pack(side="bottom")
    popup.mainloop()


add = tk.Button(
    text="+",
    font=("Arial", 60),
    height=3,
    width=4,
    command=increase
)
add.pack(side="right")


menubar = Menu(w)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='Reset', command=reset)
file.add_separator()
file.add_command(label='Exit', command=w.destroy)

# Adding Edit Menu and commands
edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit)
edit.add_command(label='Copy', command=copy)

about = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu=about)
about.add_command(label='About Simple Counter', command=popup)


# display Menu
w.config(menu=menubar)


w.mainloop()