from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from view import *
from tkinter import messagebox

janela = Tk()

janela.geometry("455x700")
janela.resizable(False, False)
janela.title("SISTEMA DE CADASTRO")
janela.configure(background="white")


def inserir():
    cod =  codigo.get()
    name = nome.get()
    CPF = cpf.get()
    date = data.get()
    s = sexo.get()
    ender = endereco.get()
    city = esc_cidade.get()
    UF = esc_uf.get()
    tel = telefone.get()
    e_mail = email.get()
    
    lista = [cod, name, CPF, date, s, ender, city, UF, tel, e_mail]
    
    if cod == '':
        messagebox.showerror("Erro", "Codigo não pode ser vazio")
    else:
        inserir_informacao(lista)
        messagebox.showinfo("Sucesso", "Inserido com sucesso")
        
        codigo.delete(0, 'end')
        nome.delete(0, 'end')
        cpf.delete(0, 'end')
        data.delete(0, 'end')
        sexo.set('')
        endereco.delete(0, 'end')
        esc_cidade.set(listaCidades[0])
        esc_uf.set(listaUF[0])
        telefone.delete(0, 'end')
        email.delete(0, 'end')
        
    
    mostrar()
    
    
global view

def alterar():
    try:
        view_dados = view.focus()
        view_dicionario = view.item(view_dados)
        view_lista = view_dicionario['values']
        
        valor_cod = view_lista[0]
        
        codigo.delete(0, 'end')
        nome.delete(0, 'end')
        cpf.delete(0, 'end')
        data.delete(0, 'end')
        sexo.set('')
        endereco.delete(0, 'end')
        esc_cidade.set(listaCidades[0])
        esc_uf.set(listaUF[0])
        telefone.delete(0, 'end')
        email.delete(0, 'end')
        
        codigo.insert(0, view_lista[0])
        nome.insert(0, view_lista[1])
        cpf.insert(0, view_lista[2])
        data.insert(0, view_lista[3])
        sexo.set(view_lista[4])
        endereco.insert(0, view_lista[5])
        esc_cidade.set(view_lista[6])
        esc_uf.set(view_lista[7])
        telefone.insert(0, view_lista[8])
        email.insert(0, view_lista[9])
        
        def update():
            cod =  codigo.get()
            name = nome.get()
            CPF = cpf.get()
            date = data.get()
            s = sexo.get()
            ender = endereco.get()
            city = esc_cidade.get()
            UF = esc_uf.get()
            tel = telefone.get()
            e_mail = email.get()
            
            lista = [name, CPF, date, s, ender, city, UF, tel, e_mail, valor_cod]
            
            if cod == '':
                messagebox.showerror("Erro", "Codigo não pode ser vazio")
            else:
                alterar_informacao(lista)
                messagebox.showinfo("Sucesso", "Atualizado com sucesso")
                
                codigo.delete(0, 'end')
                nome.delete(0, 'end')
                cpf.delete(0, 'end')
                data.delete(0, 'end')
                sexo.set('')
                endereco.delete(0, 'end')
                esc_cidade.set(listaCidades[0])
                esc_uf.set(listaUF[0])
                telefone.delete(0, 'end')
                email.delete(0, 'end')
            
            mostrar()
                
                
        botaoConfirmar = Button(janela, text="CONFIRMAR ALTERACAO", width=22, fg="black", bg="#17AD41", command=update)
        botaoConfirmar.place(x=120, y=35)
                
        
    except IndexError:
        messagebox.showerror("Erro", "Selecionar dados da tabela")
        

def deletar():
    try:
        view_dados = view.focus()
        view_dicionario = view.item(view_dados)
        view_lista = view_dicionario['values']
            
        valor_cod = [view_lista[0]]
        
        deletar_informacao(valor_cod)
        messagebox.showinfo("Sucesso", "Deletado com sucesso")
        
        mostrar()
        
    except IndexError:
        messagebox.showerror('Erro', 'Selecionar dados da tabela')
        
          
textCod = Label(janela, text="CODIGO", height=1, anchor=NW, font="Verdana 10 bold",bg="white" )
textCod.place(x=25, y=10)
codigo = Entry(janela, width=10, justify='left', relief=SOLID)
codigo.place(x=30, y=40)

textNome = Label(janela, text="NOME:*", font="Verdana 10 bold", bg="white")
textNome.place(x=25, y=80)
nome = Entry(janela, width=25, justify='left', relief=SOLID, font="Arial 10")
nome.place(x=30, y=110)

textCPF = Label(janela, text="CPF:*", font="Verdana 10 bold", bg="white")
textCPF.place(x=245, y=80)
cpf = Entry(janela, width=25, justify='left', relief=SOLID, font="Arial 10")
cpf.place(x=250, y=110)

textData = Label(janela, text="DATA NASCIMENTO: ", font="Verdana 10 bold", bg="white")
textData.place(x=25, y=150)
data = DateEntry(janela, width=25)
data.place(x=30, y=180)

textSexo = Label(janela, text="SEXO: ", font="Verdana 10 bold", bg="white")
textSexo.place(x=245, y=150)

sexo = StringVar()

sexoM = Radiobutton(janela, text="MASCULINO", value="M", font="Verdana 8", bg="white", variable=sexo)
sexoM.place(x=250, y=180)

sexoF = Radiobutton(janela, text="FEMININO", value="F", font="Verdana 8", bg="white", variable=sexo)
sexoF.place(x=350, y=180)

textEndereco = Label(janela, text="ENDERECO", font="Verdana 10 bold", bg="white")
textEndereco.place(x=25, y=220)
endereco = Entry(janela, width=25, justify='left', relief=SOLID,  font="Arial 10")
endereco.place(x=30, y=250)

textCidade = Label(janela, text="CIDADE", font="Verdana 10 bold", bg="white")
textCidade.place(x=245, y=220)
listaCidades = ["","Belo Horizonte","Brasília", "Curitiba", "Fortaleza", "Manaus", "Porto Alegre", "Recife", "Rio de Janeiro", "Salvador", "São Paulo"]
esc_cidade = StringVar()
esc_cidade.set(listaCidades[0])
cidade = OptionMenu(janela, esc_cidade, *listaCidades)
cidade.place(x=250, y=250)

textUf = Label(janela, text="UF", font="Verdana 10 bold", bg="white")
textUf.place(x=375, y=220)
listaUF = ["", "MG", "DF", "PR", "CE", "AM", "RS", "PE", "RJ", "BA", "SP"]
esc_uf = StringVar()
esc_uf.set(listaUF[0])
uf = OptionMenu(janela, esc_uf, *listaUF)
uf.place(x=380, y=250)

textTelefone = Label(janela, text="TELEFONE", font="Verdana 10 bold", bg="white")
textTelefone.place(x=25, y=290)
telefone = Entry(janela, width=25, justify='left', relief=SOLID,  font="Arial 10")
telefone.place(x=30, y=320)

textEmail = Label(janela, text="E-MAIL", font="Verdana 10 bold", bg="white")
textEmail.place(x=245, y=290)
email = Entry(janela, width=25, justify='left', relief=SOLID,  font="Arial 10")
email.place(x=250, y=320)

botaoInserir = Button(janela, text="INSERIR", width=8, fg="black", bg="#17AD41", command=inserir)
botaoInserir.place(x=30, y=360)

botaoAlterar = Button(janela, text="ALTERAR", width=8, fg="black", bg="#07BEF8", command=alterar)
botaoAlterar.place(x=110, y=360)

botaoLimpar = Button(janela, text="APAGAR", width=8, fg="black", bg="#FF003D", command=deletar)
botaoLimpar.place(x=190, y=360)


def mostrar():
    
    global view
    
    lista = mostrar_informacao()
    
    colunas = ["Codigo", "Nome", "CPF", "Data_de_nascimento", "Sexo", "Endereco", "Estado", "UF", "Telefone", "E-mail"]

    treeview_width = 400
    treeview_height = 250
    view = ttk.Treeview(janela, selectmode="extended", columns=colunas, show="headings")
    view.place(x=30, y=420, width=treeview_width, height=treeview_height)

    hsb = ttk.Scrollbar(janela, orient="horizontal", command=view.xview)
    hsb.place(x=30, y=670, width=420)
    view.configure(xscrollcommand=hsb.set)

    vsb = ttk.Scrollbar(janela, orient="vertical", command=view.yview)
    vsb.place(x=435, y=420, height=240)
    view.configure(yscrollcommand=vsb.set)
    
    hd = ["center", "center", "center", "center", "center", "center", "center", "center", "center", "center", "center"]
    h = [70, 150, 150, 120, 50, 150, 150, 50, 150, 150]
    n = 0
    
    for c in colunas:
        view.heading(c, text=c.title(), anchor=CENTER)
        view.column(c, width=70, anchor=hd[n])
        
        n+=1
    
    for item in lista:
        view.insert('', 'end', values=item)
    
mostrar()

janela.mainloop()