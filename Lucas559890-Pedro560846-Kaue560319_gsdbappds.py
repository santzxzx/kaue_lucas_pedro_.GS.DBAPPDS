# GS Patricia
# Lucas Ganciar 559890
# Pedro Quintana 560846
# Kaue Grigorio 560319


# Solicita a quantidade de dias
n = int(input("Insira a quantidade de dias: "))

# Variáveis de controle
total_consumo = 0
dias_cumpriram_meta = 0
dias_nao_cumpriram_meta = 0
meta_consumo = 150
maior_consumo = None
menor_consumo = None

# Entrada de dados e processamento
for i in range(1, n + 1):
    consumo = int(input(f"Insira o consumo do dia {i}: "))
    total_consumo += consumo

    # Verificação da meta
    if consumo >= meta_consumo:
        dias_cumpriram_meta += 1
    else:
        dias_nao_cumpriram_meta += 1

    # Descobrir maior e menor consumo
    if maior_consumo is None or consumo > maior_consumo:
        maior_consumo = consumo
    if menor_consumo is None or consumo < menor_consumo:
        menor_consumo = consumo

# Cálculo da média de consumo
media_consumo = total_consumo / n

# Relatório de resultados
if dias_cumpriram_meta == n:
    print("Parabéns! Todos os dias cumpriram a meta de consumo sustentável.")
elif dias_cumpriram_meta == 0:
    print("Infelizmente, nenhum dia cumpriu a meta de consumo sustentável.")
else:
    print(f"{dias_cumpriram_meta} dias cumpriram a meta e {dias_nao_cumpriram_meta} dias não cumpriram a meta.")
print(f"A média de consumo foi de {media_consumo:.2f} kWh. O maior consumo foi de {maior_consumo} kWh e o menor consumo foi de {menor_consumo} kWh.")
