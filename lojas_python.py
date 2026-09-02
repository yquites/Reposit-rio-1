import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()

vendedores = {"Abebe" : 1, "Gustavo" : 2, "Rodrigo" : 3}
num_vendas = 0
dindin_total = 0
vendas_por_vendedor = {}
maior_venda = 0
vendedor_maior_venda = "Não houve vendas valoráveis."

def encontrar_vendedor(codigo): 
    for nome, numero in vendedores.items():
        if numero == codigo:
            return nome

def tela_venda():
    print("=="*20)
    print("Olá! Bem-vindo(a) às Lojas Python's!")
    print("=="*20)

while True:
    try:
        tela_venda()
        vendedor = int(input("Digite o código do vendedor que lhe atendeu: "))

        if vendedor == 0:
            limpar_tela()
            break

        if vendedor not in vendedores.values():
            print("Código não reconhecido!")
            input("Tente novamente. Digite ENTER para continuar.")
            limpar_tela()
            continue

        nome_vendedor = encontrar_vendedor(vendedor)
        num_vendas += 1
        #Aqui, ocorre a relação entre o parâmetro  "código" e o return "nome".
            #Isso porque a máquina trata o input "vendedor(int)" como o tal "código".
                #Logo, se o código é = ao número daquele vendedor, o sistema me retorna seu "nome", como já especificado na função "encontrar_vendedor".
            #O parâmetro a ser analisado na resposta do cliente é a variável "vendedor(int)", parâmetro esse que será lido e comparado perante ao dicionário criado anteriormente.

        limpar_tela()
            
        print(f"Vendedor: {nome_vendedor}.")
        valor = float(input("Insira o valor da compra: "))

        if valor <= 0:
            print("Não é possível realizar uma venda com valor igual ou abaixo de 0.")
            input("Tente novamente. Digite ENTER para continuar.")
            limpar_tela()
            while num_vendas > 0:
                num_vendas -= 1
            else:
                num_vendas = 0
            continue
            #Isto impede vendas irreais.

        if valor > maior_venda:
            maior_venda = valor
            vendedor_maior_venda = nome_vendedor
            #Neste "if" o que ocorre é o seguinte:
                #Nossa variável "maior_venda" começa com valor zerado, para que assim, de acordo com as vendas feitas durante a execução do código a variável seja constamente comparada com a variável "valor" e possa ser atualizada caso o último valor recebido seja maior que os anteriores.
                #E para fechar sua funcionalidade, a parte "vendedor_maior_venda = nome_vendedor" funciona assim:
                    #A variável "vendedor_maior_venda" começa como uma variável str com uma mensagem. De acordo com as vendas feitas, caso o valor de fato seja maior que os anteriores o nome da var str será atualizada de acordo com o nome encontrado atrelado ao valor recebido. E uma curiosidade: já que é possível que em algum dia vendas não sejam feitas, se o valor recebido nunca for maior que 0, a mensagem transmitida por essa variável será compatível com o contexto da situação.

        if nome_vendedor not in vendas_por_vendedor:
            vendas_por_vendedor[nome_vendedor] = 0
            #Aqui, criamos uma espécie de função, entretanto utilizando o "if". Como o dict "vendas_por_vendedores" inicia o programa completamente vazio, tanto o nome do vendedor, quanto os valores recebidos durante a execução do programa são adicionados ao longo da própria execução. Tendo como keys os nomes dos vendedores ([nome_vendedor] representa isso) e como values os valores (o 0 representa isso, entretanto com uma certa diferença da parte das keys).

        vendas_por_vendedor[nome_vendedor] += valor
            #A diferença dita antes está aqui. Como explicado antes, o value atrelado ao valor das compras de fato é criado zerado. Mas, graças a esta linha de código, toda vez que um valor for informado, o programa o armazenará no value daquela key em específico (por isso temos aqui o nome do dict novamente). O que faz isso de fato é o indicador "+=".

        dindin_total += valor

        input("Obrigado por sua compra!\nDigite ENTER para continuar.")
        limpar_tela()

    except ValueError:
        print("Digite usando apenas números!")
        input("Tente novamente. Digite ENTER continuar.")
        limpar_tela()

if num_vendas > 0:
    media = dindin_total/num_vendas
else:
    media = 0

#Final do código:
print("=="*14)
print("Resumo das ações do dia:")
print("=="*14)

print(f"Número de vendas de hoje: {num_vendas}.\n")
print(f"Valor arrecadado hoje: R${dindin_total:.2f}.\n")
print(f"Valor médio das vendas de hoje: R${media:.2f}.\n")
print(f"As vendas feitas por cada um de nossos funcionários no dia de hoje:")
for nome, total in vendas_por_vendedor.items():
    print(f"{nome}:, R${total:.2f}.")
print(f"\nHoje, nosso funcionário com maior venda foi: {vendedor_maior_venda}!\nCom uma venda no valor de R${maior_venda:.2f}.\nParabéns!\n")

input("Digite ENTER para encerrar.")
limpar_tela()
