import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

saldo = 2000
qtd_depositos = 0
qtd_saques = 0
operacoes_realizadas = 0

def tela_inicial ():
    print("==" * 15)
    print("Bem-vindo(a) ao Banco Python!")
    print("==" * 15)

    print("Escolha uma de nossas opçõe de atendimento abaixo:")
    print("Digite (1) caso queira consultar saldo;")
    print("Digite (2) caso queira depositar;")
    print("Digite (3) caso queira sacar;")
    print("Digite (4) caso queira consultar quantidade de operações;")
    print("Digite (0) caso queira encerrar.")

escolha = 0

while escolha != 0:

    tela_inicial()
    escolha = int(input("\n-> "))
    try:
        if escolha == 1:
            limpar_tela()
            print(f"O seu saldo atual é de: R${saldo}.")
            input("Digite ENTER para continuar:")
            limpar_tela()
            tela_inicial()
            escolha = int(input("\n-> "))

        elif escolha == 2:
            deposito = float(input("Digite o valor que deseja depositar: "))
            limpar_tela()

            if deposito > 0:
                saldo += deposito
                qtd_saques += 1
                operacoes_realizadas += 1
                print(f"Seu saldo atual é de: R${saldo}.")
                input("Digite ENTER para continuar:")
                limpar_tela()
                tela_inicial()
                escolha = int(input("\n-> "))

            else:
                print("Depósitos devem ser em valores positivos!")
                input("Digite ENTER para continuar:")
                limpar_tela()
                tela_inicial()
                escolha = int(input("\n-> "))


        elif escolha == 3:
            saque = float(input("Digite o valor que deseja sacar: "))
            limpar_tela()
            
            if saque > 0 and saque <= saldo:
                saldo -= saque
                operacoes_realizadas += 1
                qtd_depositos += 1
                print(f"Seu saldo atual é de: R${saldo}.")
                input("Digite ENTER para continuar:")
                limpar_tela()
                tela_inicial()
                escolha = int(input("\n-> "))                

            else:
                print("Você não pode realizar um saque neste valor.")
                input("Digite ENTER para continuar:")
                limpar_tela()
                tela_inicial()
                escolha = int(input("\n-> "))

        elif escolha == 4:
            limpar_tela()            
            print(f"Você realizou {operacoes_realizadas} operações. Elas foram:")
            print(f"{qtd_depositos} depósito(s) e {qtd_saques} saque(s).")
            input("Digite ENTER para continuar:")
            limpar_tela()
            tela_inicial()
            escolha = int(input("\n-> "))

        elif escolha > 4:
            limpar_tela()
            print("Valor inválido! Tente novamente.")
            input("Digite ENTER para continuar:")
            limpar_tela()
            tela_inicial()
            escolha = int(input("\n-> "))          
       
    except ValueError:
        limpar_tela()
        print("Valor inválido! Tente novamente.")
        input("Digite ENTER para continuar:")
        limpar_tela()
        tela_inicial()
        escolha = int(input("\n-> "))

limpar_tela()
print(f"Seu saldo atual é de R${saldo}.")
print(f"Você realizou {qtd_depositos} depositos.")
print(f"Você realizou {qtd_saques} saques.")
print(f"E realizou {operacoes_realizadas} operações.")
input("\nDigite ENTER para encerrar:")
limpar_tela()