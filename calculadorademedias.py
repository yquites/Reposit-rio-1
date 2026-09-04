#O programa principal deverá receber as notas, chamar a função, apresentar a média e informar se o
#aluno foi aprovado, ficou em recuperação ou foi reprovado.
#Desafio: criar uma segunda função situacaoAluno(media) que retorne a situação do aluno.
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

def cmedia(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

def situacao(parametro):
    if parametro >= 7:
        aprovacao = print("O aluno foi aprovado.")

    elif parametro >= 5:
        aprovacao = print("O aluno está de recuperação.")

    elif parametro < 5 and parametro >= 0: 
        aprovacao = print("O aluno foi reprovado.")
    return aprovacao

def menu():
    print("==" * 15)
    print("CALCULADORA DE MÉDIAS")
    print("==" * 15)

menu()
input("Digite ENTER para continuar:")
limpar_tela()

try:
    nota1 = float(input("Insira a primeira nota do aluno: "))

    while nota1 < 0 or nota1 > 11:
        limpar_tela()
        print("Nota inválida! Tente novamente.")
        input("Digite ENTER para continuar:")
        limpar_tela()
        nota1 = float(input("Insira a primeira nota do aluno: "))

    nota2 = float(input("Insira a segunda nota do aluno: "))

    while nota2 < 0 or nota1 > 11:
            limpar_tela()
            print("Nota inválida! Tente novamente.")
            input("Digite ENTER para continuar:")
            limpar_tela()
            nota2 = float(input("Insira a segunda nota do aluno: "))

    nota3 = float(input("Insira a terceira nota do aluno: "))

    while nota3 < 0 or nota1 > 11:
            limpar_tela()
            print("Nota inválida! Tente novamente.")
            input("Digite ENTER para continuar:")
            limpar_tela()
            nota3 = float(input("Insira a terceira nota do aluno: "))

    resultado = cmedia(nota1, nota2, nota3)

except ValueError:
        limpar_tela()
        print("Valor inválido! Tente novamente.")
        input("Digite ENTER para continuar:")
        limpar_tela()
 

print(f"A média do aluno é: {resultado:.1f} ponto(s).")
situacao(resultado)
input("Digite ENTER para encerrar:")
limpar_tela()