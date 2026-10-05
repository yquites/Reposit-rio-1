import time, os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

nums = []

def busca(lista, chave):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == chave:
            return print(f"O número {lista[meio]} foi encontrado na posição {meio}.")

        elif chave > lista[meio]:
            inicio = meio + 1

        elif chave < lista[meio]:
            fim = meio - 1

    return print("O número pedido não foi encontrado!")

def main():
    global nums

    limpar_tela()
    print("=="*10)
    print("BUSCADOR DE LISTA")
    print("=="*10)

    valido = False

    while not valido:
        try:
            qtd = int(input("Insira quantos números serão adicionados à lista: "))

            while qtd <= 0:
                print("Informe um número maior que zero.")
                input("Digite ENTER para continuar: ")
                limpar_tela()

                qtd = int(input("Insira quantos números serão adicionados à lista: "))

            valido = True

        except ValueError:
            print("Insira uma valor válido, por favor.")
            input("Digite ENTER para continuar: ")
            limpar_tela()

    while valido == True:    
        try:
            for i in range(qtd):
                numero = float(input("==> "))
                nums.append(numero)
                
            limpar_tela()

            nums.sort()

            chave = float(input("Qual número você quer descobrir a posição?\n==> "))
            
            busca(nums, chave)
            break

        except ValueError:
            
            print("Informe valores válidos, por favor.")
        
main()
        
    






    