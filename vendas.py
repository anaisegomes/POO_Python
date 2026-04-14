vendas_mensais = [
    [120, 80, 45],   # Janeiro
    [95, 110, 60],   # Fevereiro
    [130, 75, 55],   # Março
    [140, 90, 70],   # Abril
    [110, 105, 65],  # Maio
    [125, 85, 50],   # Junho
    [115, 95, 60],   # Julho
    [105, 100, 55],  # Agosto
    [135, 120, 75],  # Setembro
    [150, 110, 80],  # Outubro
    [145, 105, 70],  # Novembro
    [160, 130, 85]   # Dezembro
]

# Inicialização dos acumuladores
total_produtos = [0, 0, 0]      # índices 0,1,2 representam A,B,C
nomes_produtos = ["A", "B", "C"]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Variáveis para controle do mês com maior venda
maior_total_mes = 0
mes_maior_venda = ""
maior_valor_mes = 0

# 1. Percorre cada mês com índice para saber qual é
for i, mes in enumerate(vendas_mensais):
    # Soma total das vendas no mês (os 3 produtos)
    total_mes = sum(mes)  # também poderia ser feito com um loop interno

    # Verifica se este mês supera o recorde
    if total_mes > maior_total_mes:
        maior_total_mes = total_mes
        mes_maior_venda = meses[i]
        maior_valor_mes = total_mes

    # Acumula as vendas de cada produto
    for j in range(3):
        total_produtos[j] += mes[j]

# 2. Calcula médias
medias = [total / 12 for total in total_produtos]

# 3. Encontra o produto mais vendido (índice do maior total)
indice_mais_vendido = 0
for i in range(1, 3):
    if total_produtos[i] > total_produtos[indice_mais_vendido]:
        indice_mais_vendido = i
produto_mais_vendido = nomes_produtos[indice_mais_vendido]
total_mais_vendido = total_produtos[indice_mais_vendido]

# Exibição dos resultados
print("=== Relatório Anual de Vendas ===\n")

print("Vendas totais anuais:")
for i in range(3):
    print(f"  Produto {nomes_produtos[i]}: {total_produtos[i]} unidades")

print("\nMédia mensal de vendas:")
for i in range(3):
    print(f"  Produto {nomes_produtos[i]}: {medias[i]:.1f} unidades/mês")

print(f"\nMês com maior volume total de vendas: {mes_maior_venda}")
print(f"  Total vendido no mês: {maior_valor_mes} unidades")

print(f"\nProduto mais vendido no ano: {produto_mais_vendido}")
print(f"  Total anual: {total_mais_vendido} unidades")