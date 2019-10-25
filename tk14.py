from tkinter import *


def mostrarNome():
    vartexto.set(textbox1.get())

root = Tk()
root.title("Aplicação")

vartexto = StringVar()

label1 = Label(root, text="O teu nome é: ")
textbox1 = Entry(root)
button = Button(root, text="Executar", command=mostrarNome)
label2 = Label(root, textvariable=vartexto)

label1.grid()
textbox1.grid()
button.grid()
label2.grid()

root.mainloop()