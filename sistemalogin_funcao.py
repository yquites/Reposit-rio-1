import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

cadastros_salvos = {"adm123" : "12345"}

def validar_login ():
    limpar_tela()
    u = input("Informe seu nome de usuário: \n")
        
    if u in cadastros_salvos:
        print(f"Olá, {u}! Como é bom tê-lo de volta!")
        
        tentativas = 3

        senha_salva = cadastros_salvos[u]
        s = input("Confirme sua senha de acesso: \n")
        
        if s == senha_salva:
            print("Acesso concedido!\n")
            print(f"Bem-vindo(a) {u}!\nObrigado por sua presença em nosso site.\n")

            input("Para encerrar, digite ENTER:")
            limpar_tela()
        
        while s != senha_salva:

            while tentativas > 1:               
                tentativas -= 1
                print(f"Senha incorreta! Você ainda possui {tentativas} tentativa(s).")
                input("Digite ENTER para tentar novamente:\n  ")
                limpar_tela()
                s = input("Confirme sua senha de acesso: \n")

            else:
                print("Acesso negado!")
                input("Tente novamente mais tarde. Digite ENTER para sair: ")
                limpar_tela()
                break

    else:
        print("Usuário Inválido! Tente novamente.")
        input("Digite ENTER para continuar:")
        limpar_tela()

def menu():
    print("Olá seja bem-vindo ao Sistema Python, escolha uma das opções para continuar: ")
    print("Digite (1) para fazer o login;")
    print("Digite (2) para fazer seu cadastro;")
    print("Digite (3) para sair.")

opcao = 0

while opcao != 3:

    try:
        menu()
        opcao = int(input("-> "))       
        
        if opcao == 1:
            limpar_tela()
            validar_login()

        elif opcao == 2:
            limpar_tela()
            usuario = input("Digite um nome de usuário: ")

            while usuario in cadastros_salvos:
                print("Nome de usuário já existente! Tente novamente.")
                input("Digite ENTER para continuar:")
                limpar_tela()
                usuario = input("Digite um nome de usuário: ")

            else:
                senha = input("Digite uma senha: ")
                cadastros_salvos[usuario] = senha

                print(f"Cadastro bem sucedido! Seja bem-vindo, {usuario}.")
                input("Digite ENTER para continuar:")
                limpar_tela()                

        if opcao < 1 and opcao > 3:
            limpar_tela()
            print("Digite uma opção válida. Por favor.")
            input("Digite ENTER para continuar:")   
            limpar_tela()
            menu()
            opcao = int(input("-> "))

    except ValueError:
        limpar_tela()
        print("=" * 6); print("ERROR"); print("=" * 6)
        print("Valor inválido! tente novamente.") 
        input("Digite ENTER para continuar:")
        limpar_tela()

limpar_tela()
print("Até logo!")