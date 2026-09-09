import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

entregas_total = 0
km_total = 0
valor_total = 0
entregas_150 = 0
motoristas = {"Marcelo" : 1, "Fred" : 2, "Thiago" : 3}
entregas_por_motorista = {}
mais_entregas = 0
melhor_entregador = " "

def encontrarmotorista (codigo):
    global motoristas

    for nome, numero in motoristas.items():
        if codigo == numero:
            return nome

def maior_entregador (nome):
    global entregas_por_motorista
    for entregas in entregas_por_motorista:
        num_entregas = entregas_por_motorista[entregas]
        return num_entregas

def main():

    global entregas_total
    global km_total
    global valor_total
    global entregas_150
    global motoristas
    global entregas_por_motorista
    global mais_entregas
    global melhor_entregador

    try:
        limpar_tela()
        print("==" * 20)
        print("SISTEMA DE REGISTRO DE ENTREGAS")
        print("==" * 20)

        motorista = int(input("Insira o código identificador do motorista: "))

        while motorista > 0:
            limpar_tela()

            nome_motorista = encontrarmotorista(motorista)

            if nome_motorista not in motoristas:
                input("Motorista não identificado! Tente novamente digitando ENTER:")
                main()

            entregas_total += 1
    

            if nome_motorista not in entregas_por_motorista:
                entregas_por_motorista[nome_motorista] = 0

            entregas_por_motorista[nome_motorista] += 1

            if maior_entregador(nome_motorista) > mais_entregas:
                mais_entregas = maior_entregador(nome_motorista)
                melhor_entregador = nome_motorista

            distancia = float(input(f"Motorista: {nome_motorista};\nInsira a distância percorrida: "))

            km_total += distancia
            if distancia > 149:
                entregas_150 += 1

            valor = float(input("insira o valor recebido pela entrega: "))
            
            valor_total += valor
        
            input("\nPara continuar, digite ENTER:")
            main()

        if motorista == 0:

            if entregas_total > 0:
                media = valor_total/entregas_total
                
            else:
                media = 0

            limpar_tela()

            print("==" * 20)
            print("ESTATÍSTICAS DAS ENTREGAS DO DIA")
            print("==" * 20)        
            
            print(f"\nEntregas realizadas hoje: {entregas_total} entrega(s).") 
            print(f"Nossos motoristas percorreram hoje: {km_total} km(s) totais.") 
            print(f"O valor total arrecadado hoje foi de: R${valor_total:.2f}.") 
            print(f"O valor médio recebido por entrega hoje foi de R${media}.") 
            print(f"As entregas com distâncias acima de 150km feitas hoje foram: {entregas_150} entrega(s).")
            for nome, entregas in entregas_por_motorista.items():
                print(f"Nome: {nome}; Entregas: {entregas}")
            print(f"O entregador que mais realizou entregas foi: {melhor_entregador}, com {mais_entregas} entrega(s) realizadas. Parabéns!!!")
            input("\nPara encerrar o programa, digite ENTER:")
            limpar_tela()

    except ValueError:
        limpar_tela()
        print("Valor inválido!")
        input("Digite ENTER para tentar novamente: ")
        main()

main()