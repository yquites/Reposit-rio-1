import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

#Variáveis:
pedidos_feitos = 0
itens_vendidos = 0
faturamento = 0
valores = []

#Pratos ofertados, seus códigos e valores:
produtos = {
            1: {"prato": "Macarrão", "preco": 30.00},
            2: {"prato": "Tropeiro", "preco": 32.00},
            3: {"prato": "Lasanha", "preco": 35.00},
            4: {"prato": "Filé com fritas", "preco": 45.00}
                                                            }

def tela_inicial():
    print("==" * 20)
    print("Bem-vindo(a) ao Restaurante Python!")
    print("==" * 20)

    print("\nNosso cardápio:")
    print(" Macarrão (1) -> R$30,00")
    print(" Tropeiro (2) -> R$32,00")
    print(" Lasanha (3) -> R$35,00")
    print(" Filé com fritas (4) -> R$45,00")

while True:
    try:
        tela_inicial()

        escolha = int(input("\nInforme o código do prato escolhido: "))
        limpar_tela()

        if escolha == 0:
            limpar_tela()
            break       

        if escolha not in produtos:
            print("Prato não encontrado, tente novamente.")
            input("Digite ENTER para continuar:")
            limpar_tela()
            continue

        print(f"Prato escolhido: {produtos[escolha]["prato"]}")
        print(f"Valor unitário: {produtos[escolha]["preco"]}\n")

        quantidade = int(input("Qual a quantia de pratos?\n> "))
        itens_vendidos += quantidade

        valor = quantidade * produtos[escolha]["preco"]
        faturamento += valor
        valores.append(valor)
        print(f"O valor da compra será de: R${valor}.\n")
        input("Digite ENTER para continuar.")
        limpar_tela()

        continuacao = int(input("Você finalizou sua compra?\nSe sim, digite 1. Caso contrário, digite 2.\n> "))

        if continuacao == 1:
            print("Obrigado por sua compra! Dirija-se ao balcão para realizar o pagamento.")
            input("Digite ENTER para encerrar.")
            pedidos_feitos += 1
            limpar_tela()
            continue

        if continuacao == 2:
            limpar_tela()
            continue        

        if continuacao not in (1,2):
            print("Valor inválido! Tente novamente.")
            input("Digite ENTER para continuar:")
            limpar_tela()
            continue 

    except ValueError:
        print("Valor inválido! Tente novamente.")
        input("Digite ENTER para continuar:")
        limpar_tela()
        continue

mpedido = max(valores)

print("==" * 15)
print("ESTATÍSTICAS DO DIA")
print("==" * 15)

print(f"\nO número de clientes (pedidos) hoje foi: {pedidos_feitos}.")
print(f"O número de pratos vendidos hoje foi: {itens_vendidos}.")
print(f"Hoje, arrecadamos o valor de R${faturamento:.2f} em vendas.")
print(f"O pedido mais caro foi num valor de R${mpedido:.2f}.")
if faturamento > 3000:
    print("Batemos a meta de R$3000,00 em um único dia! Parabéns, equipe!")
input("Para encerrar as atividades de hoje, digite ENTER.")
limpar_tela()