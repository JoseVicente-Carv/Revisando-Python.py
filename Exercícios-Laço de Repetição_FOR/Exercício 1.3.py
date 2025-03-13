""" 3) Crie um programa que leia 10 números do usuário e armazene-os em uma lista. 
Em seguida, exiba a lista, o maior número contido nela, e a soma de todos os números digitados. """

numeros = []

for contador in range (5):
    numeroDigitado = float(input(f"Digite o {contador+1}º número: "))
    
    numeros.append(numeroDigitado)

for contador2 in numeros:
    print(contador2)