from tkinter import *

def comissao():
    valor = float(valorVenda.get())
    por = float(porcentagem.get())
    
    calComissao = valor * (por/100)
    
    resComissao = f"Comissão: R${round(calComissao, 2)}"
    
    resultado['text'] = resComissao
    
def valorPorcentagem():
    valTot = float(valorVenda2.get())
    valCom = float(valorComissao.get())
    
    valPor = (valCom*100)/valTot
    
    resPor = f"Porcentagem: {round(valPor, 2)}%"
    
    resultadoPor['text'] = resPor
    
janela = Tk()

janela.geometry("250x250")
janela.title("CALCULADORA DE PORCENTAGEM")

# CALCULO DE COMISSÃO 

textCalComissao = Label(janela, text="Calcular comissão:")
textCalComissao.grid(column=0, row=0)

textVenda = Label(janela, text="Valor Total: R$")
textVenda.grid(column=0, row=1)
valorVenda = Entry(janela, width=10)
valorVenda.grid(column=1, row=1)

textPorcentagem = Label(janela, text="Porcentagem: %")
textPorcentagem.grid(column=0, row=2)
porcentagem = Entry(janela, width=10)
porcentagem.grid(column=1, row=2)

botao = Button(janela, text="Calcular", command=comissao)
botao.grid(column=1, row=5)

resultado = Label(janela, text="")
resultado.grid(column=0, row=4)

# CALCULO DE PORCENTAGEM 

textValorPorcentagem = Label(janela, text="Calcular porcentagem:")
textValorPorcentagem.grid(column=0, row=6)

textVenda2 = Label(janela, text="Valor Total: R$")
textVenda2.grid(column=0, row=7)
valorVenda2 = Entry(janela, width=10)
valorVenda2.grid(column=1, row=7)

textComissao = Label(janela, text="Comissão: R$")
textComissao.grid(column=0, row=8)
valorComissao = Entry(janela, width=10)
valorComissao.grid(column=1, row=8)

botao2 = Button(janela, text="calcular", command=valorPorcentagem)
botao2.grid(column=1, row=10)

resultadoPor = Label(janela, text="")
resultadoPor.grid(column=0, row=9)

janela.mainloop()