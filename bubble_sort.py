# BUBBLE SORT
vetor = []
cont = 0

for i in range(10):
    num = int(input())
    vetor.append(num)

print(f"vetor lido: {vetor}")

for k in range(10):
    for j in range(9):
        if vetor[j] > vetor[j+1]:
            key = vetor[j]
            vetor[j] = vetor[j+1]
            vetor[j+1] = key
        cont += 1
    cont += 1

print(f"vetor ordenado: {vetor}")
print(f"comparacoes: {cont}")