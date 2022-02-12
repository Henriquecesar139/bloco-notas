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
    global diretorio
    try:
        diretorio = askopenfilename()
        conteudo = []
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
    if estilo== 3:
        texto['bg'] = 'orange'
        texto['fg'] = 'black'


def tamanho_fonte(n):
    global tamanho
    if n == 1:
        tamanho += 2
    elif n == 2:
        tamanho -= 2
    texto['font'] = (fonte_estilo, tamanho)

def tipo_fonte(n):
    global fonte_estilo
    if n == 1:
        texto['font'] = ('arial')
        fonte_estilo = 'arial'
    if n == 2:
        texto['font'] = ('courier')
        fonte_estilo = 'courier'
    if n == 3:
        texto['font'] = ('terminal')
        fonte_estilo = 'terminal'
    if n == 4:
        texto['font'] = ('roman')
        fonte_estilo = 'roman'

diretorio = ''
tamanho = 12
fonte_estilo = 'arial'

tela = Tk()
tela['bg'] = 'gray'
tela.title('Bloco De Notas')
tela.geometry('800x600')

menu = Menu(tela)

arquivo = Menu(menu)
arquivo.add_command(label="Abrir", command = abrir)
arquivo.add_command(label="Salvar", command = salvar)
arquivo.add_command(label = "sair", command = sair)
menu.add_cascade(label="Arquivo", menu=arquivo)

estilo = Menu(menu)
estilo.add_command(label = 'escuro', command = lambda : tema(1))
estilo.add_command(label = 'claro', command = lambda : tema(2))
estilo.add_command(label = 'laranja', command = lambda : tema(3))
menu.add_cascade(label="tema", menu = estilo)

fonte = Menu(menu)
fonte.add_command(label = 'Texto Maior', command = lambda : tamanho_fonte(1))
fonte.add_command(label = 'Texto Menor', command = lambda : tamanho_fonte(2))
menu.add_cascade(label = 'texto', menu = fonte)


fonte2 = Menu(menu)
fonte2.add_command(label = 'Arial', command = lambda : tipo_fonte(1))
fonte2.add_command(label = 'Courier', command = lambda : tipo_fonte(2))
fonte2.add_command(label = 'Terminal', command = lambda : tipo_fonte(3))
fonte2.add_command(label = 'Roman', command = lambda : tipo_fonte(4))
menu.add_cascade(label = 'Fonte', menu = fonte2)

tela.config(menu = menu)

texto = Text (tela, width = 180, height = 80, bg = 'white', fg = 'black')
texto.pack(side = TOP)
texto.configure(font=(fonte_estilo, tamanho))

tela.mainloop()