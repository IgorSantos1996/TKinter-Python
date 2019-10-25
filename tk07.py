from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Igor")
menu_inicial.geometry("500x500")

texto = StringVar()
texto.set("Novo Texto")

label1 = Label(menu_inicial,
    text = "Palavra",
    font="Arial 20",
    bg = "red",
    fg = "white",
    textvariable = texto
)
label1.pack()
texto.set("Igor Terriaga")

label2 = Label(menu_inicial,
    text = "Palavra",
    font="Arial 20",
    bg = "red",
    fg = "white",
    textvariable = texto
)
label2.pack()
label3 = Label(menu_inicial,
    text = "Palavra",
    font="Arial 20",
    bg = "red",
    fg = "white",
    textvariable = texto
)
label3.pack()
label4 = Label(menu_inicial,
    text = "Palavra",
    font="Arial 20",
    bg = "red",
    fg = "white",
    textvariable = texto
)
label4.pack()


menu_inicial.mainloop()