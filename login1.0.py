# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando
# uma mensagem de erro e voltando a pedir as informações.

while True:
    nomeUsuario = str(input("Usuário: "))
    senha = str(input("Senha: "))

    if nomeUsuario != senha:
        print("Login valido!")
        break
    else:
        print("Login invalido!  (USUARIO IGUAL A SENHA)\n")
        continue

