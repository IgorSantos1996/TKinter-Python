from tkinter import *

menu_principal = Tk()
menu_principal.title("Titulo")
menu_principal.geometry("500x500")

label = Label(
    menu_principal,
    text = "Frase de testes\niGOR",
    font = "Arial 20",
    bd = 1,
    relief = "solid",
    width = 55,
    height = 5,
    anchor = S # alinhar o texto ao sul
).pack()


label = Label(
    menu_principal,
    text = "Frase de testes",
    font = "Arial 20",
    bd = 1,
    relief = "solid",
    width = 25,
    height = 4,
    anchor = S, # alinhar o texto ao sul
    padx = 50,
    pady = 50,
    justify = CENTER
).pack()

menu_principal.mainloop()