#Sistema de Consumo de Energia

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()

def consumo():

    while True:
        try:
            
            consumos = []
            total = 0
            meses = [ "janeiro",
                    "fevereiro", 
                    "março", 
                    "abril", 
                    "maio", 
                    "junho",
                    "julho",
                    "agosto",
                    "setembro",
                    "outubro",
                    "novembro",
                    "dezembro" ]
                
            print("Olá! Esse é seu sistema de consumo de energia anual.\n Siga os comandos a seguir:\n")

            for i in range (len(meses)):
                valor = float(input(f"Insira o consumo mensal do mês de {meses[i]}: \n"))

                consumos.append(valor)

                total = total + valor

                media = total/12

            maiorconsumo = max(consumos)
            menorconsumo = min(consumos)

            for i in range(len(consumos)):
                if consumos[i] == maiorconsumo:
                 mes_maior = meses[i]

            print(f"O seu gasto anual foi:\n R${total:.2f}.\n")
            print(f"Sua média mensal no ano foi:\n R${media:.2f}.\n")
            print(f"O maior consumo entre os meses foi no mês de {mes_maior}, com o valor de:\n R${maiorconsumo:.2f}.\n")
            print(f"O menor consumo entre os meses foi no valor de:\n R${menorconsumo:.2f}. ")

            break                

        except ValueError:
            print("Entrada Inválida! Use apenas números!")

consumo()
