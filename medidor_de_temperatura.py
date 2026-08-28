semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
lista_temp = []
temp_30 = 0
temp_total = 0
qtd_dias = 7



for dia in semana:
    temp_dia = float(input(f"Insira a temperatura de {dia}: "))
    temp_total = temp_total + temp_dia
    lista_temp.append(temp_dia)
    media = temp_total/qtd_dias
    maior_temp = max(lista_temp)
    posicao_maior = lista_temp.index(maior_temp)
    dia_maior = semana[posicao_maior]
    if temp_dia > 30:
            temp_30 = temp_30 + 1


print(f"\nO total de graus celcius da semana foi: {temp_total}°.")
print(f"A temperatura média foi de: {media:.1f}°.")
print(f"A maior temperatura ocorreu {dia_maior} e foi de: {maior_temp}.")
print(f"A menor temperatura foi de: {min(lista_temp)}°.")
print(f"A quantia de dias com temperatura maior que 30° foi de: {temp_30}.")