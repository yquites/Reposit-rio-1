import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

def opcoes():
    print("==" * 15)
    print("Bem-vindo à Biblioteca Python!")
    print("==" * 15)
    print("\nEscolha uma de nossas opções abaixo:\n")
    print("Para pegar livro emprestado aperte (1)")
    print("Para devolver livro emprestado aperte (2)")
    print("Para consultar a quantia de livros disponíveis aperte (3)")
    
limpar_tela()

livros_total = 100
livros_emprestados = 0
devolucao = 0
emprestimos = 0

while True:
    try:
        opcoes()
        opcao = int(input("\n> "))

        if opcao == 0:
            limpar_tela()
            break

        if opcao > 3:
            limpar_tela()
            print("Opção inválida!")
            input("Digite ENTER para continuar:")
            limpar_tela()
            continue
                    
        if opcao == 1:
            limpar_tela()
            if livros_total > 0:
                emprestimos =+ 1
                livros_emprestados =+ 1
                livros_total = livros_total - 1
                print(f"Você pegou um livro emprestado! Restam {livros_total} livros disponíveis.")
                input("Digite ENTER para sair:")
                limpar_tela()
                continue
            else:
                print("Quantia de livros insuficientes!\nTente novamente mais tarde.")
                input("Digite ENTER para sair:")
                limpar_tela()
                continue

        if opcao == 2:
            limpar_tela()
            if livros_total < 100:
                devolucao =+ 1
                livros_total = livros_total + 1
                print(f"Você devolveu um livro! Agora temos {livros_total} livros disponíveis.")
                input("Digite ENTER para sair:")
                limpar_tela()
                continue
            else:
                print("Não existem livros emprestados.")
                input("Digite ENTER para sair:")
                limpar_tela()
                continue
               

        if opcao == 3:
            limpar_tela()
            print("A quatidade de livros disponíveis é:")
            print(f"{livros_total} livros(s).")
            input("Digite ENTER para continuar:")
            limpar_tela()
            continue

    except ValueError:
        limpar_tela()
        print("Utilize apenas números de 1-3!")
        input("Digite ENTER para continuar:")
        limpar_tela()

    print(f"A quantidade de livros emprestados foi de: {emprestimos}.")
    print(f"A quantidade de livros devolvidos foi de: {devolucao}.")
    print(f"A quantidade de livros disponíveis é de: {livros_total}.")