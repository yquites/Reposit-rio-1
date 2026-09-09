# 1. Controle de consumo de água em um condomínio
# Um condomínio deseja acompanhar o consumo de água de seus apartamentos durante um mês. 
# Para cada apartamento, informe o número do apartamento, a quantidade de moradores e o consumo em m³.
# A tarifa possui três faixas: até 10 m³: R$ 4,50 por m³; de 11 a 20 m³: R$ 6,00 por m³; acima de 20 m³: R$ 8,50 por m³. 
# Para simplificar, considere que todo o consumo do apartamento será calculado pela tarifa correspondente à sua faixa.
# O cadastro termina quando o número do apartamento for 0.
# Ao final, o valor total das contas, o consumo médio por apartamento e o apartamento com maior consumo.
# Desafio: apresentar também quantos apartamentos ultrapassaram 20 m³ e o percentual deles em relação ao total.
import os
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
limpar_tela()
time.sleep(0.1)

apartamentos = 0
cons_total = 0
valor_total = 0
ap_maior20 = 0
maior_valor = 0

def calcularvalor (v):
    global ap_maior20
    if v < 10:
        value = v * 4.5

    elif v > 10 and v < 20:
        value = v * 6

    else:
        value = v * 8.5
        ap_maior20 +=1
    return value  

def main():
    try:
        global maior_valor
        global apartamentos
        global cons_total
        global valor_total
        global ap_maior20
        global maior_consumidor

        limpar_tela()

        print("==" * 15)
        print("CONTROLE DE CONSUMO DE ÁGUA")
        print("==" * 15)

        apartamento = int(input("\nInsira o bloco e número do apartamento (ex: 123); para encerrar, digite '0'.\n> "))
        
        while apartamento > 0:
        
            limpar_tela ()
            apartamentos += 1
            
            print("==" * 15)
            print(f"CÁLCULO DO AP {apartamento}")
            print("==" * 15)

            quantia_agua = float(input("Insira o consumo de água em m³: "))
            cons_total += quantia_agua
            valor = calcularvalor(quantia_agua)

            if valor > maior_valor:
                maior_valor = valor
                maior_consumidor = apartamento

            valor_total += valor
            print(f"O valor a ser pago pelo AP {apartamento} é R${valor:.2f}.\n")

            input("Para continuar a operação, digite ENTER: ")
            main()

        else:
            limpar_tela()

            if apartamentos > 0:
                mediaagua = cons_total/apartamentos
                mediavalor = valor_total/ apartamentos
            else:
                mediaagua = 0
                mediavalor = 0                

            if ap_maior20 > 0:
                porcentagem = (ap_maior20/apartamentos) * 100

            else:
                porcentagem = 0    

            print("==" * 15)
            print("RESUMO ESTATÍSTICO DO MÊS")
            print("==" * 15)

            print(f"Os {apartamentos} apartamentos registrados nesse mês consumiram {cons_total}m³ de água. ")
            print(f"O valor total a ser pago pelo condomínio é de R${valor_total:.2f}.")
            print(f"O consumo médio por condômino foi de {mediaagua}m³ de água e a média de valor foi de R${mediavalor:.2f} ")
            print(f"O apartamento com maior consumo foi o AP {maior_consumidor},\n e pagarão uma conta num valor de R${maior_valor:.2f} ")
            print(f"A quantidade de apartamentos que ultrapassaram a marca de 20m³ de gastos foram {ap_maior20} aparatamento(s),\n e a representação porcentual sobre o toal é de {porcentagem:.1f}%.")

            input("Para encerrar, digite ENTER:")
            limpar_tela()

    except ValueError:
        limpar_tela()
        input("Valor inválido! Para tentar novamente, digite ENTER: ")
        main()    

main()