import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

estoque = { "Água Mineral" : 50,
            "Salgadinho" : 30,
            "Cerveja" : 15,
            "Pct de arroz" : 20,
            "Vinho Rosé" : 5,
            "Vaso de flor" : 8,
            "Pct de café" : 12,
            "Salaminho" : 20,
            "Vassoura" : 3,
            "Lâmpada" : 30
}

prod_cod = { "Água Mineral" : 1,
            "Salgadinho" : 2,
            "Cerveja" : 3,
            "Pct de arroz" : 4,
            "Vinho Rosé" : 5,
            "Vaso de flor" : 6,
            "Pct de café" : 7,
            "Salaminho" : 8,
            "Vassoura" : 9,
            "Lâmpada" : 10
}

def encontar_produto(codigo):
    for prod, cod in prod_cod.items():
        if cod == codigo:
            return prod

def maior_estoque():
    global maior_prod; global maior_qtd
    maior_qtd = 0
    maior_prod = ""

    for produto, quantidade in estoque.items():
        if quantidade > maior_qtd:
            maior_qtd = quantidade
            maior_prod = produto
            return maior_prod

def main():
    global maior_prod; global maior_qtd
    limpar_tela()
    print("=== CONTROLE DE ESTOQUE ===")
    print("(1) - Ver estoque\n(2) - Ver maior estoque\n(3) - Estoques que precisam de reasbatecimento\n(4) - Sair")

    try:
        opcao = int(input(">"))

        if opcao == 1:
            limpar_tela()
            print("=== ESTOQUE ===\n")

            for produtos, quantidades in estoque.items():
                print(f"Produto: {produtos}; Quantidade: {quantidades}")

            input("\nPara voltar ao menu principal, digite ENTER: ")
            main()

        elif opcao == 2:
            maior_estoque()
            print(f"\nProduto de maior estoque: {maior_prod}; Quantidade: {maior_qtd}")
            input("\nPara continuar, digite ENTER:")
            main()

        elif opcao == 3:
            limpar_tela()
            print("=== PRODUTOS EM FALTA ===\n")
            for produto, quantidade in estoque.items():
                if quantidade < 10:
                    print(f"Produto: {produto}; Quantidade: {quantidade}")

            input("\nPara voltar ao menu principal, digite ENTER: ")
            main()

        elif opcao == 4:
            limpar_tela()
            print("FIM")

        elif opcao < 1 and opcao > 4:
            limpar_tela()
            print("Opção inválida! Tente novamente.")
            input("Digite ENTER para continuar:")
            main()            

    except ValueError:
        limpar_tela()
        print("Valor inválido! Tente novamente.")
        input("Digite ENTER para continuar:")
        main()
main()