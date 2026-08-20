import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()


def postogas():


    veiculos = 0
    litrostotal = 0
    valor = 0
    mais40 = 0



    print("Bem-vindo ao posto Python! Siga as instruções abaixo: ")

    litros = float(input("Quantos litros você deseja abastecer?\n (Valor do combustível: R$ 5,00):\n "))

    while litros > 0:
        try:
            litrostotal = litrostotal + litros
            veiculos = veiculos + 1
            valor = litrostotal * 5

            if litros > 40:
                mais40 = mais40 + 1

            litros = float(input("Quantos litros você deseja abastecer? "))

        except ValueError:
            print("Utilize apenas números, por favor.")

            
    if veiculos > 0:
        media = litrostotal/veiculos

    else:
        media = 0
    
    print(f"O total de veículos que abasteceram foi de {veiculos}.\n")
    print(f"O total de litros abastecidos foi de {litrostotal} litros.\n")
    print(f"O valor arrecadado foi: R${valor}.\n")
    print(f"A média de litros abastecidos por veículo foi de {media: .2f} litros.\n")
    print(f"O total de veículos que abasteceram mais de 40 litros foi de {mais40} veículos.\n")
    
postogas()