""" 8) Faça um programa que percorra duas vetores/listas e gere uma terceira vetor/lista sem elementos repetidos. """

numeros1 = [2,4,6,8,9,10]
numeros2 = [2,5,7,8,11,13]

# numeros3 = numeros1 + numeros3

numeros3 = set(numeros1 + numeros2)

print(numeros3)