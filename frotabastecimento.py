import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

num_abastecimentos = 0
media_pagamentos = []
litros_total = 0
valor_total = 0
km_total = 0
maior_abastecimento = 0

def precolitromedio (p, l):
    preco_por_litro = p/l
    return preco_por_litro

def main():
    global num_abastecimentos
    global pagamentos
    global media_pagamentos
    global litros_total
    global valor_total
    global km_total
    global maior_abastecimento

    limpar_tela()

    print("==" * 20)
    print("SISTEMA DE REGISTRO DE ABASTECIMENTOS")
    print("==" * 20)

    placa = input("Informe a placa do veículo: ").lower()

    if placa != "fim":
        try:
            limpar_tela()

            num_abastecimentos += 1

            km_atual = float(input("Insira a quilometragem atual do veículo: "))
            km_total += km_atual

            litros_abastecidos = float(input("Insira a quantidade de litros de combustível abastecidos ao longo da viagem: "))
            litros_total += litros_abastecidos

            valor_pago = float(input("Informe qual valor total gasto na viagem: "))

            if valor_pago > maior_abastecimento:
                maior_abastecimento = valor_pago

            valor_total += valor_pago

            preco_medio = precolitromedio(valor_pago, litros_abastecidos)
            media_pagamentos.append(preco_medio)
            print(f"O preço médio por litro abastecido foi de R${preco_medio:.2f}.")

            input("Digite ENTER para continuar: ")
            main()

        except ValueError:
            limpar_tela()
            print("Valor inválido!")
            input("Digite ENTER para tentar novamente: ")
            main()

main()
limpar_tela()

if litros_total > 0:
    media = valor_total/litros_total
else:
    media = 0    

print("==" * 20)
print("SISTEMA DE REGISTRO DE ABASTECIMENTOS")
print("==" * 20)

print(f"\nHoje registramos:\n{num_abastecimentos} abastecimento(s);")
print(f"{litros_total} litros abastecido(s);")
print(f"R${valor_total:.2f} gastos em abastecimentos;")
print(f"o valor médio gasto por litro foi: {media:.2f}R$/L; ")
print(f"O abastecimento mais caro de hoje ocorreu num valor de R${maior_abastecimento:.2f},")
print("Pagamentos que superaram a média geral de valor por litro:")
for pagamentos in media_pagamentos:
    if pagamentos > media:
        print(f"R${pagamentos:.2f}")

input("\nPara encerrar o programa, digite ENTER: ")
limpar_tela()
