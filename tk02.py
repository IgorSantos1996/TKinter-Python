from tkinter import *

menu_inicial = Tk()
menu_inicial.title("Titulo da janela amigão")
#menu_inicial['bg'] = "blue"  background azul
menu_inicial.geometry("500x300")

def cmd_click(mensagem):
    print(mensagem)


# Definindo um botão
btn = Button(menu_inicial, text="Executar",  command=lambda: cmd_click("Igor"))
btn.pack()
# Definindo outro botão
cmd =  Button(menu_inicial, text="Clicar", command = lambda:cmd_click("Outra mensagem"))
cmd.pack()
menu_inicial.mainloop()
