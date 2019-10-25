from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Titulo")
menu_inicial.geometry("500x300")

label = Label(menu_inicial, text="Este é o label 1", font = "Arial 20", bd = 10, relief="solid")
label.pack()
label = Label(menu_inicial, text="Este é o label 1", font = "Arial 20", bd = 10, relief="groove")
label.pack()
label = Label(menu_inicial, text="Este é o label 1", font = "Arial 20", bd = 10, relief="flat")
label.pack()
label = Label(menu_inicial, text="Este é o label 1", font = "Arial 20", bd = 10, relief="raised")
label.pack()
label = Label(menu_inicial, text="Este é o label 1", font = "Arial 20", bd = 10, relief="sunken")
label.pack()
menu_inicial.mainloop()