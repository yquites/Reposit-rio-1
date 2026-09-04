import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

veiculos = 0
valor_total = 0

def calcularEstacionamento (h):
    if h <= 1:
        v = 8
    if h > 1 and h <= 3:
        v = 15
    if h > 3:
        v = 20
    return v

def menu ():
    print("==" * 15)
    print("CALCULADORA DO ESTACIONAMENTO:")
    print("Até 1 hora = R$ 8,00")
    print("Até 3 horas = R$ 15,00")
    print("Mais de 3 horas = R$ 20,00")
    print("==" * 15)

try:
    menu()
    codigo = int(input("Escolha a opção desejada:\n(1) - Calcular pagamento\n(2) - Encerrar atividades\n\n> "))

    while codigo != 2:

        if codigo == 1:
            limpar_tela()
            horas = float(input("Informe quantas horas o veículo permaneceu no estabelecimento: "))
            veiculos += 1
            valor = calcularEstacionamento(horas)
            valor_total += valor
            print(f"O valor a ser pago é de R$ {valor:.2f}.")

            input("Digite ENTER para continuar")
            limpar_tela()
            menu()
            codigo = int(input("Escolha a opção desejada:\n(1) - Calcular pagamento\n(2) - Encerrar atividades\n\n> "))

        if codigo not in (1, 2):
            limpar_tela()
            print("Valor inválido! Tente novamente.")
            input("Digite ENTER para sair:")
            limpar_tela()
            menu()
            codigo = int(input("Escolha a opção desejada:\n(1) - Calcular pagamento\n(2) - Encerrar atividades\n\n> "))

except ValueError:
    limpar_tela()
    print("Valor inválido! Tente novamente.")
    input("Digite ENTER para sair:")
    limpar_tela()
    menu()
    codigo = int(input("Escolha a opção desejada:\n(1) - Calcular pagamento\n(2) - Encerrar atividades\n\n> "))

if veiculos > 1:
     media = valor_total/veiculos
else:
     media = 0

limpar_tela()
print("==" * 15)
print("ESTATÍSTICAS DO DIA:")
print("==" * 15)

print(f"O total de veículos de hoje foi: {veiculos} veículo(s).")
print(f"O faturamento de hoje foi de: R${valor_total:.2f}.")
print(f"O valor médio pago por veículo hoje foi de: {media:.2f}")

input("Digite ENTER para encerrar:")
limpar_tela()