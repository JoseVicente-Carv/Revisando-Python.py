""" 1) Crie um programa que receba três números e imprima o maior deles. """

# importe a biblioteca necessaria.
import os

# Crie um vetor.
numeros = []

os.system('cls || clear') # limpar a tela do terminal.

# crier um laço de repetição para o usuario colocar numeros dentro do vetor
for contador in range(3): #laço de repetição x3
    numeroDigitado = float(input(f"Digite o {contador+1}º número: ")) # pedir um numero ao usuario
    
    numeros.append(numeroDigitado) #colocar o numero dentro do vetor

# mostre o maior numero digitado
os.system('cls || clear') # limpar a tela do terminal.
print(f"O maior número digitado foi: {max(numeros)}")