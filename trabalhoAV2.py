from tkinter import *
import back as back

selected_tuple = 'none'

def get_selected_row(event):
    global selected_tuple
    index = lista.curselection()[0]
    selected_tuple = lista.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])


def view():
    lista.delete(0, END)
    for row in back.view():
        lista.insert(END, row)


def procurar():
    lista.delete(0, END)
    for row in back.search(nomealuno.get(), nomemateria.get(), notaaluno.get()):
        lista.insert(END, row)


def adicionar():
    while(nomealuno.get() != "" and nomemateria.get() != "" and notaaluno.get() != ""):
        back.insert(nomealuno.get(), nomemateria.get(),
                    notaaluno.get(),)
        lista.delete(0, END)
        lista.insert(END, (nomealuno.get(), nomemateria.get(),
                        notaaluno.get(),))
        # Limpando as informações na entry
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

        view()
    else:
        nomealuno.set("Preencha o campo")
        nomemateria.set("Preencha o campo")
        notaaluno.set("Preencha o campo")

def deletar():
    back.delete(selected_tuple[0])
    # Limpando as informações na entry
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    view()

def atualizar():
    back.update(selected_tuple[0], nomealuno.get(
    ), nomemateria.get(), notaaluno.get())
    # Limpando as informações na entry
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    view()

root = Tk()
root.title("Sistema de cadastro e consulta de notas de alunos")
width = 750
height = 300
# colectando informacoes do monitor
sc_width = root.winfo_screenwidth()
sc_height = root.winfo_screenheight()
x = (sc_width/2) - (width/2)
y = (sc_height/2) - (height/2)
# tamanho da janela principal
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg='gray85')

l1 = Label(root, text="Nome do Aluno", bg='gray85', fg='#000000')
l1.grid(row=0, column=1)
l2 = Label(root, text="Nome da Materia", bg='gray85', fg='#000000')
l2.grid(row=1, column=1)
l3 = Label(root, text="Nota", bg='gray85', fg='#000000')
l3.grid(row=2, column=1)

nomealuno = StringVar()
e1 = Entry(root, textvariable=nomealuno)
e1.grid(row=0, column=2)
nomemateria = StringVar()
e2 = Entry(root, textvariable=nomemateria)
e2.grid(row=1, column=2)
notaaluno = StringVar()
e3 = Entry(root, textvariable=notaaluno)
e3.grid(row=2, column=2)



lista = Listbox(root, height=10, width=60)
lista.grid(row=8, column=1, rowspan=6, columnspan=2)

sb1 = Scrollbar(root)
sb1.grid(row=8, column=3, rowspan=6)

lista.configure(yscrollcommand=sb1.set)
sb1.configure(command=lista.yview)

lista.bind('<<ListboxSelect>>', get_selected_row)

b7 = Button(root, text="Procurar", width=22, bg="royal blue1", command=procurar)
b7.grid(row=1, column=4)

b1 = Button(root, text="Exibir", width=22,
            bg="snow", command=view)
b1.grid(row=9, column=4)

b4 = Button(root, text="Atualizar",
            width=22, bg="gold", command=atualizar)
b4.grid(row=9, column=5)

b3 = Button(root, text="Adicionar", width=22, bg="royal blue1", command=adicionar)
b3.grid(row=10, column=4)

b5 = Button(root, text="Deletar",
            bg="firebrick4", width=22, command=deletar)
b5.grid(row=10, column=5)

""" Deixando opcao sair do programa em comentario por design"""
# b6 = Button(root, text="Sair do Programa", width=22, bg="red", command=root.destroy)
# b6.grid(row=8, column=5)

root.mainloop()
