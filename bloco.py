from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

def salvar():
    global diretorio
    try:
        if diretorio == '':
            diretorio = asksaveasfilename()
        arq = open(diretorio, 'w')
        arq.write(texto.get("1.0", END))
    except:
        pass

def abrir():
    try:
        diretorio = askopenfilename()
        conteudo = []
        print(diretorio)
        arq = open(diretorio, 'r')
        for linha in arq:
            conteudo.append(linha)
        texto.delete("1.0", END)
        texto.insert('insert' ,'\n'.join(conteudo))
    except:
        pass


def sair():
    tela.destroy()

def tema(estilo):
    if estilo == 1:
        texto['bg'] = 'black'
        texto['fg'] = 'white'
    if estilo == 2:
        texto['bg'] = 'white'
        texto['fg'] = 'black'

diretorio = ''

tela = Tk()
tela['bg'] = 'gray'
tela.title('Bloco De Notas')
tela.geometry('900x700')

menu = Menu(tela)

arquivo = Menu(menu)
arquivo.add_command(label="Abrir", command = abrir)
arquivo.add_command(label="Salvar", command = salvar)
arquivo.add_command(label = "sair", command = sair)
menu.add_cascade(label="Arquivo", menu=arquivo)

estilo = Menu(menu)
estilo.add_command(label = 'escuro', command = lambda : tema(1))
estilo.add_command(label = 'claro', command = lambda : tema(2))
menu.add_cascade(label="tema", menu = estilo)

tela.config(menu = menu)

texto = Text (tela, width = 180, height = 80, bg = 'white', fg = 'black')
texto.pack(side = TOP)


tela.mainloop()