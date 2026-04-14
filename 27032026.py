numeros = [12, 5, 8, 21, 17, 9, 14, 6, 19, 10]

# Passo 1: Calcular a soma total

soma = 0

for num in numeros:
    soma += num

# Passo 2: calcular a media

media = soma / len(numeros)

# Passo 3: Contar quantos são maiores que a media

contagem = 0
if num > media:
    contagem += 1

# Exibir resultados

print(f"Media: {media:.2f}")
print(f"Numeros acima da media: {contagem}")