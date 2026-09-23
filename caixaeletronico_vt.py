import os
import time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

#Notas disponíveis no caixa:
notas100 = 10
notas50 = 10
notas20 = 10
notas10 = 10

def sacar(valor_pedido):
    global notas100; global notas50; global notas20; global notas10; global saquepositivo

    if valor_pedido > 0:

        while notas100 > 0 and notas50 > 0 and notas20 > 0 and notas10 > 0:

            #notas de 100
            notas100usadas = valor_pedido // 100
            restante100 = valor_pedido % 100
            #notas de 50
            notas50usadas = restante100 // 50
            restante50 = restante100 % 50
            #notas de 20
            notas20usadas = restante50 // 20
            restante20 = restante50 % 20
            #notas de 10
            notas10usadas = restante20 // 10
            restante10 = restante20 % 10

        else:
            saquepositivo == False

        if restante10 > 0:
            saquepositivo = False

        else:
            saquepositivo = True    
            notas100 = notas100 - notas100usadas
            if notas100 < 0:
                saquepositivo == False          
            notas50 = notas50 - notas50usadas
            if notas50 < 0:
                saquepositivo == False                    
            notas20 = notas20 - notas20usadas
            if notas20 < 0:
                saquepositivo == False                 
            notas10 = notas10 - notas10usadas
            if notas10 < 0:
                saquepositivo == False                 
        
def main():
    global notas100; global notas50; global notas20; global notas10; global saquepositivo

    limpar_tela()
    print("====== CAIXA ELETRÔNICO =======")

    try:
        escolha = int(input("Aperte (1) para sacar\nAperte (2) para checar as notas disponíveis no caixa\nAperte (3) para sair\n> "))

        if escolha == 1:
            limpar_tela()
            print("====== SAQUE ======")

            try:
                valor_saque = int(input("Insira o valor de seu saque pretendido: "))
                sacar(valor_saque)

                if saquepositivo == True:
                    print(f"Saque de R${valor_saque:.2f} debitado de sua conta.\n")
                    input("Para continuar, aperte ENTER: ")
                    main()

                elif saquepositivo == False:
                    print(f"Saque de R${valor_saque:.2f} não realizado!")
                    input("Para tentar novamente ou sair, aperte ENTER: ")
                    main()

            except ValueError:
                limpar_tela()
                print("Valor inválido!")
                input("Tente novamente apertando ENTER: ")
                main()

        elif escolha == 2:
            limpar_tela()
            print("====== NOTAS DISPONÍVEIS ======")
            print(f"Notas de R$100,00 disponíveis: {notas100}")
            print(f"Notas de R$50,00 disponíveis: {notas50}")
            print(f"Notas de R$20,00 disponíveis: {notas20}")
            print(f"Notas de R$10,00 disponíveis: {notas10}")

            input("Se terminou, aperte ENTER para continuar: ")
            main()

        elif escolha == 3:
            print("\nAté a próxima!")

        if escolha > 3 and escolha < 1:
            limpar_tela()
            print("Erro! Opção inválida!")
            input("Aperte ENTER e tente novamente: ")
            main()

    except ValueError:
        limpar_tela()
        print("Erro! Opção inválida!")
        input("Aperte ENTER e tente novamente: ")
        main()

main()