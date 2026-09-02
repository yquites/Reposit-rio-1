import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()

aprovados = 0
recuperacao = 0
reprovados = 0
medias = []
num_alunos = 0

while True:
    try:
        
        print("==" * 10)
        print("SISTEMA DE NOTAS")
        print("==" * 10)

        nome = input("Informe o nome do aluno (digite 0 para encerrar): ")

        if nome == "0":
            limpar_tela()
            break
                
        nota1 = float(input("Informe a primeira nota: \n"))
        nota2 = float(input("Informe a segunda nota: \n"))
        nota3 = float(input("Informe a terceira nota: \n"))

        input("Digite ENTER para calcular a média do aluno: ")
        num_alunos += 1
        limpar_tela()
            
        media = (nota1 + nota2 + nota3) / 3
        medias.append(media)
        print(f"A média foi computada!\nO aluno obteve {media:.1f} pontos.")

        if media >= 7:
            aprovados += 1
            print("O aluno foi aprovado.")

        elif media >= 5 and media < 7:
            recuperacao += 1
            print("O aluno está de recuperaçaõ.")

        else:
            reprovados += 1
            print("O aluno foi reprovado.")

        input("Digite ENTER para continuar:")
        limpar_tela()
    except ValueError:
        print("Valor inválido!\nTente novamente.")
        input("Digite ENTER para continuar:")
        limpar_tela()
        continue

if num_alunos > 0:
    media_total = sum(medias)
    mediag = media_total / num_alunos
    maiorm = max(medias)
    menorm = min(medias)
else:
    mediag = 0
    maiorm = 0
    menorm = 0


print("==" * 20)
print("ESTATÍSTICAS DA TURMA")
print("==" * 20)

print(f"O número de alunos aprovados foi de: {aprovados}")
print(f"O número de alunos em recuperação é: {recuperacao}")
print(f"O número de alunos reprovados foi: {reprovados}")
print(f"A média geral foi de: {mediag:.1f} pontos.")
print(f"A maior média foi de: {maiorm:.1f} pontos.")
print(f"A menor média foi de: {menorm:.1f} pontos.")

input("Digite ENTER para encerrar:")
limpar_tela()