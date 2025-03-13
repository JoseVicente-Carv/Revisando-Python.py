""" 2) Escreva um programa que leia números inteiros do usuário até que o número 0 seja digitado. 
Ao final, exiba a soma desses números."""

numeros = [] #crie um vetor

while True: 
    numeroDigitado = int(input(f"Digite um número: "))
    
    if (numeroDigitado == 0):
        break
    else:
        numeros.append(numeroDigitado)

print("Soma dos numeros digitados:", sum(numeros))