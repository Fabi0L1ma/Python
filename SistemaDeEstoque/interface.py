from tkinter import *
from tkinter import ttk
from banco import *
from tkinter import messagebox

banco = sqlite3.connect('produtos.db')

janela = Tk()

janela.geometry("900x600")
janela.resizable(False, False)
janela.title("Gerenciador de Estoque")

style = ttk.Style()
style.configure("TMenubutton", background="lightblue")


def inserir():
    cod = cod_prod.get()
    marca = marca_prod.get()
    modelo = modelo_prod.get()
    preco = preco_prod.get()
    ano = ano_prod.get()
    cor = esc_cor.get()
    filial = filial_prod.get()
    data_entrada = entrada_prod.get()
    data_saida = saida_prod.get()
    
    lista = [cod, marca, modelo, preco, ano, cor, filial, data_entrada, data_saida]
    
    if cod == '':
        messagebox.showerror("Erro", "Codigo não pode ser vazio")
    else:
        inserir_informacao(lista)
        messagebox.showinfo("Sucesso", "Inserido com sucesso")
        
        cod_prod.delete(0, 'end')
        marca_prod.delete(0, 'end')
        modelo_prod.delete(0, 'end')
        preco_prod.delete(0, 'end')
        ano_prod.delete(0, 'end')
        esc_cor.set(listaCores[0])
        filial_prod.delete(0, 'end')
        entrada_prod.delete(0, 'end')
        saida_prod.delete(0, 'end')
    
    mostrar()
    
global view

def alterar():
    try:
        view_dados = view.focus()
        view_dicionario = view.item(view_dados)
        view_lista = view_dicionario['values']
        
        valor_cod = [view_lista[0]]
        
        cod_prod.delete(0, 'end')
        marca_prod.delete(0, 'end')
        modelo_prod.delete(0, 'end')
        preco_prod.delete(0, 'end')
        ano_prod.delete(0, 'end')
        esc_cor.set(listaCores[0])
        filial_prod.delete(0, 'end')
        entrada_prod.delete(0, 'end')
        saida_prod.delete(0, 'end')
        
        cod_prod.insert(0, view_lista[0])
        marca_prod.insert(0, view_lista[1])
        modelo_prod.insert(0, view_lista[2])
        preco_prod.insert(0, view_lista[3])
        ano_prod.insert(0, view_lista[4])
        esc_cor.set(view_lista[5])
        filial_prod.insert(0, view_lista[6])
        entrada_prod.insert(0, view_lista[7])
        saida_prod.insert(0, view_lista[8])
        
        def update():
            cod = cod_prod.get()
            marca = marca_prod.get()
            modelo = modelo_prod.get()
            preco = preco_prod.get()
            ano = ano_prod.get()
            cor = esc_cor.get()
            filial = filial_prod.get()
            data_entrada = entrada_prod.get()
            data_saida = saida_prod.get()
            
            lista = [marca, modelo, preco, ano, cor, filial, data_entrada, data_saida] + valor_cod

            
            #lista = [marca, modelo, preco, ano, cor, filial, data_entrada, data_saida, valor_cod]
            
            if cod == '':
                messagebox.showerror("Erro", "Codigo não pode ser vazio")
            else:
                alterar_informacao(lista)
                messagebox.showinfo("Sucesso", "Atualizado com sucesso")
                
                cod_prod.delete(0, 'end')
                marca_prod.delete(0, 'end')
                modelo_prod.delete(0, 'end')
                preco_prod.delete(0, 'end')
                ano_prod.delete(0, 'end')
                esc_cor.set(listaCores[0])
                filial_prod.delete(0, 'end')
                entrada_prod.delete(0, 'end')
                saida_prod.delete(0, 'end')
                
            mostrar()
            
        botaoConfirmar = Button(janela, text="CONFIRMAR ALTERAÇÃO", background="#228B22", fg="white", width=25, relief=GROOVE, command=update)
        botaoConfirmar.place(x=680, y=530)
            
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
            
        
text_titulo = Label(janela, text="GERENCIAMENTO DE PRODUTOS", fg="#029CDB", font="28")
text_titulo.place(x=280, y=30)

text_cod = Label(janela, fg="black", text="CODIGO: ")
text_cod.place(x=45, y=100)
cod_prod = ttk.Entry(janela, width=10)
cod_prod.place(x=45, y=120)

text_Marca = Label(janela, fg="black", text="MARCA: ")
text_Marca.place(x=150, y=100)
marca_prod = ttk.Entry(janela, width=20)
marca_prod.place(x=150, y=120)

text_Modelo = Label(janela, fg="black", text="MODELO: ")
text_Modelo.place(x=310, y=100)
modelo_prod = ttk.Entry(janela, width=20)
modelo_prod.place(x=310, y=120)

text_Preco = Label(janela, fg="black", text="PREÇO: ")
text_Preco.place(x=475, y=100)
preco_prod = ttk.Entry(janela, width=20)
preco_prod.place(x=475, y=120)

text_ano = Label(janela, fg="black", text="ANO: ")
text_ano.place(x=635, y=100)
ano_prod = ttk.Entry(janela, width=10)
ano_prod.place(x=635, y=120)

text_cor = Label(janela, fg="black", text="COR: ")
text_cor.place(x=735, y=100)
listaCores = ["", "PRETO", "BRANCO", "PRATA", "VERMELHO", "AZUL"]
esc_cor = StringVar()
esc_cor.set(listaCores[0])
cor = ttk.OptionMenu(janela, esc_cor, *listaCores)
cor.place(x=735, y=120)

text_filial = Label(janela, fg="black", text="FILIAL: ")
text_filial.place(x=45, y=170)
filial_prod = ttk.Entry(janela, width=20)
filial_prod.place(x=45, y=190)

text_dataEntrada = Label(janela, fg="black", text="ENTRADA: ")
text_dataEntrada.place(x=200, y=170)
entrada_prod = ttk.Entry(janela)
entrada_prod.place(x=200, y=190)

text_saida = Label(janela, fg="black", text="SAIDA: ")
text_saida.place(x=355, y=170)
saida_prod = ttk.Entry(janela)
saida_prod.place(x=355, y=190)

botaoInserir = Button(janela, text="INSERIR", background="#228B22", fg="white", width=10, relief=GROOVE, command=inserir)
botaoInserir.place(x=580, y=190)

botaoAlterar = Button(janela, text="ALTERAR", background="#1E90FF", fg="white", width=10, relief=GROOVE, command=alterar)
botaoAlterar.place(x=670, y=190)

botaoDeletar = Button(janela, text="DELETAR", background="red", fg="white", width=10, relief=GROOVE, command=deletar)
botaoDeletar.place(x=760, y=190)


botaoConfirmar = Button(janela, text="CONFIRMAR ALTERAÇÃO", background="#228B22", fg="white", width=25, relief=GROOVE)
botaoConfirmar.place(x=680, y=530)

def mostrar():
    global view
    
    lista = mostar_informacao()

    colunas = ["CODIGO", "MARCA", "MODELO", "PREÇO", "ANO", "COR", "FILIAL", "ENTRADA", "SAIDA"]

    treeview_width = 840
    treeview_height = 250
    view = ttk.Treeview(janela, selectmode="extended", columns=colunas, show="headings")
    view.place(x=30, y=250, width=treeview_width, height=treeview_height)

    vsb = ttk.Scrollbar(janela, orient="vertical", command=view.yview)
    vsb.place(x=875, y=250, height=250)
    view.configure(yscrollcommand=vsb.set)
    
    hd = ["center", "center", "center", "center", "center", "center", "center", "center", "center"]
    h = [70, 150, 150, 120, 50, 150, 150, 50, 150, 150, 150]
    n = 0
    
    for c in colunas:
        view.heading(c, text=c.title(), anchor=CENTER)
        view.column(c, width=70, anchor=hd[n])
        
        n+=1
    
    for item in lista:
        view.insert('', 'end', values=item)
        
mostrar()
    
janela.mainloop()