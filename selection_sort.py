# SELECTION SORT
vetor = []
ordenado = []
cont = 0

for i in range(10):
    num = int(input())
    vetor.append(num)
print(f"vetor lido: {vetor}")

while len(ordenado) != 10:
    menor = vetor[0]
    posicao = 0
    for j in range(1,len(vetor)):  
        if vetor[j] < menor:
            menor = vetor[j]
            posicao = j
        cont += 1
    cont += 1
    ordenado.append(menor)
    vetor.remove(menor)

print(f"vetor ordenado: {ordenado}")
print(f"comparacoes: {cont}")