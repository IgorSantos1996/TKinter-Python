from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Primeira app")

menu_inicial.geometry("500x250+200+200") #largura altura posicaox posicaoy
menu_inicial.resizable(True, True) # não ajusta largura, não ajusta altura se tiver como False
menu_inicial.iconbitmap("Graph.ico")

menu_inicial.minsize(width = 500, height =  250) # ajustar somente até esses valores (liimites)
menu_inicial.maxsize(width = 700, height = 400) # ajustar somente até esses valores (limites)

# menu_inicial.state("zoomed") #automaticamente maximiza
# menu_inicial.state("iconic") # fica só o icone

menu_inicial.mainloop()