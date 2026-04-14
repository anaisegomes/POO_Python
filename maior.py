a = float(input())
b = float(input())
c = float(input())

maior = a

if (b > maior):
    maior = b
if (c > maior):
    maior = c

print("Maior: ", maior)



menor = a

if (b < menor):
    menor = b
if (c < menor):
    menor = c

print("Menor: ", menor)
