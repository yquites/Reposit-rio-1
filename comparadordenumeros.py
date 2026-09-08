import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

numeros = []

def maiordois (a, b):
    numeros.append(a); numeros.append(b)
    maior = max(numeros)
    return maior

def menordois (a, b):
    numeros.append(a); numeros.append(b)
    return min(numeros)

def menordez (c, d, e, f, g, h, i, j, k, l):
    numeros.append(c); numeros.append(d); numeros.append(e); numeros.append(f); numeros.append(g)
    numeros.append(h); numeros.append(i); numeros.append(j); numeros.append(k); numeros.append(l)
    return min(numeros)

def maiordez (c, d, e, f, g, h, i, j, k, l):
    numeros.append(c); numeros.append(d); numeros.append(e); numeros.append(f); numeros.append(g)
    numeros.append(h); numeros.append(i); numeros.append(j); numeros.append(k); numeros.append(l)
    return max(numeros)

def telainicial ():
    print("==" * 20)
    print("Bem-vindo(a) ao comparador de números!")
    print("==" * 20)
    print("\nEscolha uma de nossas opções:\n" \
    "(1) Comparar o maior número entre dois;\n" \
    "(2) Comparar menor número entre dois;\n" \
    "(3) Compara maior número entre dez;\n" \
    "(4) Comparar menor número entre dez;\n" \
    "(5) Sair.")

codigo = 0

while codigo != 5:

    try:
        telainicial()
        codigo = int(input("\n> "))

        if codigo == 1:
            limpar_tela()
            print("Comparador de tamanho entre dois números.\n")
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            print(f"O maior número é {maiordois(num1, num2)}.")
            input("Para continuar, digite ENTER:")
            numeros.clear()
            limpar_tela()

        if codigo == 2:
            limpar_tela()
            print("Comparador de tamanho entre dois números.\n")
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            print(f"O menor número é {menordois(num1, num2)}.")
            input("Para continuar, digite ENTER:")
            numeros.clear()
            limpar_tela()

        if codigo == 3:
            limpar_tela()
            print("Comparador de tamanho entre dez números.\n")
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            num3 = float(input("Insira o terceiro número: "))
            num4 = float(input("Insira o quarto número: "))
            num5 = float(input("Insira o quinto número: "))
            num6 = float(input("Insira o sexto número: "))
            num7 = float(input("Insira o sétimo número: "))
            num8 = float(input("Insira o oitavo número: "))
            num9 = float(input("Insira o nono número: "))
            num10 = float(input("Insira o décimo número: "))

            print(f"O maior número é {maiordez(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)}.")
            input("Para continuar, digite ENTER:")
            numeros.clear()
            limpar_tela()

        if codigo == 4:
            limpar_tela()
            print("Comparador de tamanho entre dez números.\n")
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))
            num3 = float(input("Insira o terceiro número: "))
            num4 = float(input("Insira o quarto número: "))
            num5 = float(input("Insira o quinto número: "))
            num6 = float(input("Insira o sexto número: "))
            num7 = float(input("Insira o sétimo número: "))
            num8 = float(input("Insira o oitavo número: "))
            num9 = float(input("Insira o nono número: "))
            num10 = float(input("Insira o décimo número: "))

            print(f"O menor número é {menordez(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)}.")
            input("Para continuar, digite ENTER:")
            numeros.clear()
            limpar_tela()           
                    
    except ValueError:
        limpar_tela()
        print("Valor inválido, tente novamente: ")    
        input("Para continuar, digite ENTER:")
        limpar_tela()

limpar_tela()
print("Até logo!")