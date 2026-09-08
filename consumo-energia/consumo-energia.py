
# Valor fixo da tarifa por kWh
TARIFA_KWH = 0.75

# Entrada de dados
while True:
    print("\n-------------------------------------------")
    aparelho = input("Digite o nome do aparelho (ou 'sair' para encerrar): ")

    if aparelho.lower() == 'sair':
        print("\nPrograma encerrado. Até logo!")
        break


    while True:
        try:
            potencia = float(input("Digite a potência do aparelho em watts (W): "))
            break
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido para a potência.")
            
    while True:
        try:
            horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
            break
        except ValueError:
            print("Erro: Por favor, digite valores numéricos válidos.")
    
    # Cálculo do consumo mensal (considerando 30 dias)
    consumo_mensal = (potencia * horas_dia * 30) / 1000

    # Cálculo do custo estimado
    custo_estimado = consumo_mensal * TARIFA_KWH

    # Exibição do resultado
    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo mensal estimado: {consumo_mensal:.2f} kWh")
    print(f"Custo mensal estimado: R$ {custo_estimado:.2f}")
    