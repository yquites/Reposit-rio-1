import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()


def sistema():

    salariob = 0
    salarios = []
    quantidade = 0
    folha = 0

    nome = input("Informe o nome do funcionário (para encerrar digite 0): ")

    while nome != "0":
        try:
            
            salariob = float(input("Informe o valor do salário bruto: "))
            quantidade = quantidade +1

            horaex = int(input("Informe a quantia de horas extras: "))
            salariof = salariob + (horaex * 25)
            salarios.append(salariof)
            folha = folha + salariof

            nome = input("Informe o nome do próximo funcionário (para encerrar digite 0): ")
        except ValueError:
            print("Valor inválido")
    
    if quantidade >= 1: 
            
        maior_salario = max(salarios)                                                                                                         
        menor_salario = min(salarios)
        media =  folha/quantidade

        print(f"\nQuantidade de funcionário: {quantidade}\n")
        print(f"Média dos salários: {media:.2f}\n")
        print(f"O maior salário foi: {maior_salario}\n")
        print(f"O menor salário foi: {menor_salario}")

    else:
        print("Nenhum funcionário foi resgistrado.")

sistema()