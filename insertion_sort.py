# INSERTION SORT
vetor = []
cont = 0

for i in range(10):
    num = int(input())
    vetor.append(num)

print(f"vetor lido: {vetor}")

for j in range(1,10):
    key = vetor[j]
    while key < vetor[j-1] and j > 0:
        vetor[j] = vetor[j-1]
        vetor[j-1] = key
        j -= 1
        cont += 1
    cont += 1

print(f"vetor ordenado: {vetor}")
print(f"comparacoes: {cont}")