from tkinter import *
from tkinter import messagebox

loginCad = []
senhaCad = []

def autenticar():
    loginV = str(login.get())
    senhaV = str(senha.get())
        
    if loginV == "fabio" and senhaV == "123456":
        messagebox.showinfo("LOGIN",  "LOGIN EFETUADO COM SUCESSO!")
    else:
        messagebox.showinfo("LOGIN",  "LOGIN OU SENHA INCORRETA!")
        
        
janela = Tk()

janela.geometry("300x300")
janela.title("LOGIN")
janela.configure(background= "white")

textTitulo = Label(janela, text="LOGIN", font= "verdana 18", bg= "white", fg= "black")
textTitulo.place(x=10, y=10)

linha = Label(janela, width=275, bg="#00bfff", font="verdana 1")
linha.place(x=10, y=50)

textLogin  = Label(janela, text="LOGIN *", bg="white")
textLogin.place(x=10, y=70)
login = Entry(janela, width=25, font="16", relief="solid")
login.place(x=10, y=100)

textSenha = Label(janela, text="SENHA *", bg="white")
textSenha.place(x=10, y=150)
senha = Entry(janela, width=25, font="16", show="*", relief="solid")
senha.place(x=10, y=180)

botao = Button(janela, text="ENTRAR", width=38, height=2, fg="white", bg="#00bfff", command= autenticar)
botao.place(x=10, y=230)

janela.mainloop()