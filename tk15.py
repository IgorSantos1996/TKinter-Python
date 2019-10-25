from tkinter import *

def mostrarNome():
    nome = textbox_1.get()
    label_final = Label(root, text="O teu nome é: " + nome)
    label_final.grid()

root = Tk()
root.title("Titulo da app")
root.geometry("200x100")


# criar ps widgtes

label_1 = Label(root, text="Escreve seu nome: ")
textbox_1 = Entry(root)
button_1 = Button(root, text="Executar", command=mostrarNome)

label_1.grid()
textbox_1.grid()
button_1.grid()

root.mainloop()