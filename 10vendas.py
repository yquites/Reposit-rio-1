import os
import time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

vendas = []
maior_valor = 0
total_vendido = 0
vendas_100 = 0

def comparador(n):                                                                                      
    global maior_valor
    global menor_valor
                                                                          
    if n > maior_valor:
        maior_valor = n

    menor_valor = vendas[0]

    for venda in vendas:
        if venda < menor_valor:
            menor_valor = venda

for i in range(10):
    try:
        valor = float(input("Informe o valor da venda: "))

        while valor <= 0:
            limpar_tela()
            
            print("Informe um valor válido por favor.")
            input("Digite ENTER para continuar:  ")

            limpar_tela()
            
            valor = float(input("Informe o valor da venda: "))    

        total_vendido += valor

        vendas.append(valor)

        comparador(valor)

        if valor > 100:
            vendas_100 += 1

        limpar_tela()

    except ValueError:
        print("Digite um valor válido por favor.")

if len(vendas) > 0:
    media = total_vendido/len(vendas)
else:
    media = 0

print("==============TELA DE RESUMOS=============")
print(f"\nTotal vendido: {total_vendido:.2f}")
print(f"Média de vendas: {media:.2f}")
print(f"Vendas acima de R$100,00: {vendas_100}")
print(f"Maior venda: {maior_valor:.2f}")
print(f"Menor venda: {menor_valor:.2f}")