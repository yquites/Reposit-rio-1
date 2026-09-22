import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

limpar_tela()

aprovados = 0
reprovados = 0
recuperacao = 0
medias = []
alunos = []

def calcular_media(nota1, nota2):
    global aprovados
    global reprovados
    global recuperacao

    media = (nota1 + nota2) / 2

    medias.append(media)

    if media >= 7:
        aprovados += 1

    elif media >= 5:
        recuperacao += 1

    else:
        reprovados += 1

    return media

def maior_media(a, b):
    global maior
    global alunom
    
    maior = a[0]
    alunom = b[0]

    for i in range(len(a)):
        
        if a[i] > maior:
            
            maior = a[i]
            alunom = b[i]

def main():
    global aprovados; global reprovados; global recuperacao; global medias; global maior; global alunom; global alunos
    limpar_tela()

    print("==================== SISTEMA DE NOTAS ====================")

    try:
        num_de_alunos = int(input("Insira o número de alunos a serem analisados: "))

        for n in range(num_de_alunos):
            nota1 = float(input(f"Insira a primeira nota do aluno {n + 1}: "))
                    
            while nota1 > 10:
                limpar_tela()
                print("Notas maiores que 10 não são possíveis!")
                input("Digite ENTER para prosseguir: ")
                limpar_tela()
                nota1 = float(input(f"Insira a primeira nota do aluno {n + 1}: "))    
                                                    
            while nota1 < 0:
                limpar_tela()
                print("Notas negativas não são possíveis!")
                input("Digite ENTER para prosseguir: ")
                limpar_tela()
                nota1 = float(input(f"Insira a primeira nota do aluno {n + 1}: "))

            nota2 = float(input(f"Insira a segunda nota do aluno {n + 1}: "))

            while nota2 > 10:
                limpar_tela()
                print("Notas maiores que 10 não são possíveis!")
                input("Digite ENTER para prosseguir: ")
                limpar_tela()
                nota2 = float(input(f"Insira a segunda nota do aluno {n + 1}: "))

            while nota2 < 0:
                limpar_tela()
                print("Notas negativas não são possíveis!")
                input("Digite ENTER para prosseguir: ")
                limpar_tela()
                nota2 = float(input(f"Insira a segunda nota do aluno {n + 1}: "))

                media_final = calcular_media(nota1, nota2)

                cod_aluno = n + 1
                alunos.append(cod_aluno)

                if media_final >= 7:
                    print(f"A média do aluno é: {media_final:.1f}.\nSua situação é: APROVADO.")

                elif media_final >= 5:
                    print(f"A média do aluno é: {media_final:.1f}.\nSua situação é: EM RECUPERAÇÃO.")

                else:
                    print(f"A média do aluno é: {media_final:.1f}.\nSua situação é: REPROVADO.")

                input("Para continuar, digite ENTER: ")
                limpar_tela()       
                
            if num_de_alunos > 0:
                somamedias = sum(medias)
                mediageral = somamedias/num_de_alunos
                    
                maior_media(medias, alunos)
                    
            else:
                mediageral = 0

            print(f"A quantidade de alunos que foram aprovados foi de {aprovados} alunos.")
            print(f"A quantidade de alunos que ficaram em recuperação foi de {recuperacao} alunos.")
            print(f"A quantidade de alunos reprovados foi de {reprovados} alunos.")
            print(f"A média geral da sala é de: {mediageral:.1f} ponto(s).")
            print(f"A maior média foi {maior}, que pertence ao aluno {alunom}.")

    except ValueError:
        limpar_tela()
        print("Insira um número de alunos válidos.")
        input("Digite ENTER para continuar: ")
        main()
        
main()