""" 1) Crie um programa que receba três números e imprima o maior deles. """

import os

os.system("cls || clear")

# incie o vetor
numeros = []

# receba tres numeros
for contador in range(3): # inice um laço de repetição x3
    numeroDigitado = float(input(f"Digite o {contador+1}º número: ")) #peçla o numero ao usuario

    numeros.append(numeroDigitado) #armazene o numero digitado no vetor

# mostre o maior numero no vteor
os.system("cls || clear")
print(f"O maior número digitado é {max(numeros)}.")