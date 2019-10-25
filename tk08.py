from tkinter import *

# grid manager

menu_inicial = Tk()
menu_inicial.title("Titulo")
menu_inicial.geometry("500x500")

label1 = Label(menu_inicial, text = "label1", bg = "red")
label2 = Label(menu_inicial, text = "label1", bg = "green")
label3 = Label(menu_inicial, text = "label1", bg = "blue")

#label1.pack()
#label2.pack()

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
btn1 = Button(menu_inicial, text="Click")
btn2 = Button(menu_inicial, text="Click")
btn3 = Button(menu_inicial, text="Click")

btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)


menu_inicial.mainloop()
