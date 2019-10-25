# grid manager

from tkinter import *

root = Tk()

root.title("Login")
root.geometry("200x200")

Label(root, text="Usuario: ").grid(row=0, sticky=W)
Label(root, text="Senha: ").grid(row=1, sticky=W)

Entry(root).grid(row=0, column=1)
Entry(root).grid(row=1, column=1)

Button(root, text="Login").grid(row=2, column=1, sticky=E)


root.mainloop()