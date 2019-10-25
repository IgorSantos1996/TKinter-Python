# grid manager
from tkinter import *

root = Tk()

root.title("Sem titulo por enquanto XD")
root.geometry("400x400")

Label(root, text="texto1",width=20, bg="red").grid()
Label(root, text="texto2",width=20, bg="green").grid(column=1)
Label(root, text="texto3",width=40, bg="blue").grid(column=2, sticky='we')

root.mainloop()