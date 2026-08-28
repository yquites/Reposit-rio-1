import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()

veiculos_total = 0
horas_total = 0
faturamento = 0
veiculo_3 = 0
valores_pagos = []


#Início do código
def tabela():
    print("Olá bem-vindo ao Estacionamento Python!\nNossa tabela de valores é a seguinte:\n")

    #Tabela de preços
    print("==="*20)
    print("Até 1 hora: R$ 10,00\nDe 1-3 hora(s): R$18,00\nAcima de 3 horas: R$ 30,00 (fixos) + R$ 5,00 (por hora)")
    print("==="*20)

#Informe sua placa
tabela()
placa = str(input("\nInforme a placa de seu veículo: ")).lower()

#Definições de valores
while placa != "fim":
    try:
        veiculos_total = veiculos_total + 1
        horas = float(input("Informe a quantia de horas que seu veículo permaneceu no estabelecimento: "))
        horas_total = horas_total + horas

        if horas <= 1:
            valor = 10
            valores_pagos.append(valor)
            print(f"O valor a ser pago é de: R${valor}\nDirija-se ao balcão!")
            input("Digite 'Enter' para sair.")          
            limpar_tela()
            tabela()
            placa = str(input("\nInforme a placa de seu veículo: ")).lower()

        elif horas > 1 and horas <= 3:
            valor = 18
            valores_pagos.append(valor)
            print(f"O valor a ser pago é de: R${valor}\nDirija-se ao balcão!")
            input("Digite 'Enter' para sair.")
            limpar_tela()
            tabela()          
            placa = str(input("\nInforme a placa de seu veículo: ")).lower()

        else:
            valor = 30 + (horas * 5)
            veiculo_3 = veiculo_3 + 1
            valores_pagos.append(valor)
            print(f"O valor a ser pago é de: R${valor}\nDirija-se ao balcão!")
            input("Digite 'Enter' para sair.")
            limpar_tela()
            tabela()
            placa = str(input("\nInforme a placa de seu veículo: ")).lower()

    except ValueError:
        print("Utilize apenas números!")
        limpar_tela()
#Variáveis que devem permanecer fora, mas depois de onde o código acontece
faturamento = sum(valores_pagos)
maior_valor = max(valores_pagos)

#Final do código
if placa == "fim":
    limpar_tela()
    print(f"A clientela de hoje foi de:\n {veiculos_total} veículo(s).\n")
    print(f"O faturamento total do dia de hoje foi:\n R${faturamento}.\n")
    print(f"Hoje, a quantidade de veículos que permaneceram acima de 3 horas foi de:\n {veiculo_3} veículo(s).\n")
    print(f"O maior valor de hoje foi de:\n R${maior_valor}.")