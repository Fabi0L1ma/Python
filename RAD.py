from tkinter import *
from tkinter import ttk 
import sqlite3

janela = Tk()

janela.geometry("575x700")
janela.title("SISTEMA DE CADASTRO")
janela.configure(background="white")

textCod = Label(janela, text="CODIGO", font="arial 10 bold",bg="white" )
textCod.place(x=30, y=10)
codigo = Entry(janela, width=9, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
codigo.place(x=30, y=40)

botaoBuscar = Button(janela, text="BUSCAR", width=10, fg="black", bg="#17AD41")
botaoBuscar.place(x=150, y=40)

botaoLimpar = Button(janela, text="LIMPAR", width=10, fg="black", bg="#FF003D")
botaoLimpar.place(x=240, y=40)

textNome = Label(janela, text="NOME:*", font="arial 10 bold", bg="white")
textNome.place(x=30, y=80)
nome = Entry(janela, width=30, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
nome.place(x=30, y=110)

textCPF = Label(janela, text="CPF:*", font="arial 10 bold", bg="white")
textCPF.place(x=350, y=80)
cpf = Entry(janela, width=20, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
cpf.place(x=350, y=110)

textData = Label(janela, text="DATA NASCIMENTO: ", font="arial 10 bold", bg="white")
textData.place(x=30, y=150)
data = Entry(janela, width=15, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
data.place(x=30, y=180)


textIdade = Label(janela, text="IDADE: ", font="arial 10 bold", bg="white")
textIdade.place(x=220, y=150)
idade = Entry(janela, width=5, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
idade.place(x=220, y=180)

textSexo = Label(janela, text="SEXO: ", font="arial 10 bold", bg="white")
textSexo.place(x=350, y=150)

sexo = StringVar()

sexoM = Radiobutton(janela, text="MASCULINO", value="masculino", font="time 8 bold", bg="white", variable=sexo)
sexoM.place(x=350, y=180)

sexoF = Radiobutton(janela, text="FEMININO", value="feminino", font="time 8 bold", bg="white", variable=sexo)
sexoF.place(x=450, y=180)

textEndereco = Label(janela, text="ENDERECO", font="arial 10 bold", bg="white")
textEndereco.place(x=30, y=220)
endereco = Entry(janela, width=30, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
endereco.place(x=30, y=250)

textCidade = Label(janela, text="CIDADE", font="arial 10 bold", bg="white")
textCidade.place(x=350, y=220)
cidade = Entry(janela, width=10, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
cidade.place(x=350, y=250)

textUf = Label(janela, text="UF", font="arial 10 bold", bg="white")
textUf.place(x=480, y=220)
uf = Entry(janela, width=5, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
uf.place(x=480, y=250)

textTelefone = Label(janela, text="TELEFONE", font="arial 10 bold", bg="white")
textTelefone.place(x=30, y=290)
telefone = Entry(janela, width=30, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
telefone.place(x=30, y=320)

textEmail = Label(janela, text="E-MAIL", font="arial 10 bold", bg="white")
textEmail.place(x=350, y=290)
email = Entry(janela, width=20, font="arial 12", bd=1, highlightbackground="black", highlightcolor="black", highlightthickness=1)
email.place(x=350, y=320)

botaoBuscar = Button(janela, text="BUSCAR", width=10, fg="black", bg="#17AD41")
botaoBuscar.place(x=30, y=360)

botaoBuscar = Button(janela, text="BUSCAR", width=10, fg="black", bg="#17AD41")
botaoBuscar.place(x=120, y=360)

botaoLimpar = Button(janela, text="LIMPAR", width=10, fg="black", bg="#FF003D")
botaoLimpar.place(x=210, y=360)

colunas = ("Codigo", "Nome", "CPF", "Data_de_nascimento", "Idade", "Sexo", "Endereco", "Estado", "UF", "Telefone", "E-mail")

treeview_width = 500
treeview_height = 250
view = ttk.Treeview(janela, columns=colunas, show="headings")
view.place(x=30, y=420, width=treeview_width, height=treeview_height)

hsb = ttk.Scrollbar(janela, orient="horizontal", command=view.xview)
hsb.place(x=30, y=670, width=520)
view.configure(xscrollcommand=hsb.set)

vsb = ttk.Scrollbar(janela, orient="vertical", command=view.yview)
vsb.place(x=535, y=420, height=240)
view.configure(yscrollcommand=vsb.set)

view.heading("#1", text="Codigo")
view.heading("#2", text="Nome")
view.heading("#3", text="CPF")
view.heading("#4", text="Data de nacimento")
view.heading("#5", text="Idade")
view.heading("#6", text="Sexo")
view.heading("#7", text="Endereco")
view.heading("#8", text="Cidade")
view.heading("#9", text="UF")
view.heading("#10", text="Telefone")
view.heading("#11", text="E-mail")

view.column("#1", width=70)
view.column("#2", width=150)
view.column("#3", width=150)
view.column("#4", width=120)
view.column("#5", width=50)
view.column("#6", width=50)
view.column("#7", width=150)
view.column("#8", width=150)
view.column("#9", width=50)
view.column("#10", width=150)
view.column("#11", width=150)

janela.mainloop()