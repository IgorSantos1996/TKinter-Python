from tkinter import *


menu_inicial = Tk()
menu_inicial.title("Titulo")
menu_inicial.geometry("500x300")

label01 = Label(menu_inicial, text = "Este é o label 1.", bg="yellow", fg="red", font="Times 20")
label01.pack()

label02 = Label(menu_inicial, text = "Este é o label 2.")
label02.pack()

cmd = Button(menu_inicial, text = "Executar")
cmd.pack()

menu_inicial.mainloop()
