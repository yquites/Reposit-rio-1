# 25. Sistema de vendas com funções
# Uma loja deseja registrar várias vendas. Para cada venda, informe quantidade de produtos e preço unitário.
# Crie uma função calcularVenda(quantidade, preco) que retorne o valor total da venda.
# Crie também uma função verificarMeta(total) que informe se a venda atingiu uma meta de R$ 500,00.
# O programa continua até que a quantidade informada seja 0.
# Ao final, apresente quantidade de vendas, faturamento total, média das vendas, maior venda e quantidade de vendas que atingiram a meta

import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

faturamento = 0
vendas = []
vendas500 = 0
numvendas = 0
faturamento = 0

def verificarmeta(t):
    global vendas500
    if t > 500:
        vendas500 += 1
        print("Meta de R$500,00 atingida!")
    else:
        print("Meta não cumprida.")    

def calcularvenda (q, p):
    subtotal = q * p
    return subtotal

def main():
    global vendas500
    global vendas
    global numvendas
    global faturamento

    try:
        limpar_tela()
        print("==" * 15)
        print("SISTEMA DE CAIXA REGISTRADORA")
        print("==" * 15)

        quantidade = int(input("Informe a quantia de produtos: "))

        if quantidade > 0:

            numvendas += 1

            valoruni = float(input("Insira o valor unitário do produto: "))

            total = calcularvenda(quantidade, valoruni)
            print(f"O valor total da compra é de R${total:.2f}")
            faturamento += total
            verificarmeta(total)
            vendas.append(total)
            
            input("\nPara continuar, digite ENTER:")
            main()


        else:
            maiorv = max(vendas)
            if numvendas > 0:
                media = faturamento/numvendas
            else:
                media = 0

            limpar_tela()
            print("==" * 12)
            print("RESUMO DAS ATIVIDADES")
            print("==" * 12)
            
            print(f"O valor arrecadado hoje foi de R${faturamento:.2f};")
            print(f"A quantia de vendas hoje foi de {numvendas} venda (s);")
            print(f"O valor médio por venda hoje foi de R${media:.2f};")
            print(f"A maior venda de hoje foi de R${maiorv};")
            print(f"As vendas que cumpriram a meta de R$500,00 hoje foi de R${vendas500};")

            input("Para reiniciar o caixa, digite ENTER: ")
            main()

    except ValueError:
        limpar_tela()
        input("Valor inválido! Tente novamente apertando ENTER:")
        main()

main()