""" crie um jogo de adivinhação de um número 

o usuário terá de adivinhar um número entre 1 e 100, 
o sistema deve informar se o número advinhado é maior ou menor que o objetivo, 
os sistema deve informar quantas tentativas levou até acertar. """

# importe as bibliotecas necessarias
import os
import random

os.system("cls || clear") # limpe a tela

# inicie a variavel pra registrar o numero de tentativas
tentativas: int = 0

# dfina o numero aleatorio a ser advinhado
numeroObjetivo: int = random.randint(1, 100)
# print(numeroObjetivo)

while True:
    numeroDigitado: int = int(input("Advinhe o número (ou digite 0 para desistir): "))
    tentativas += 1

    if (numeroDigitado == 0):
        print(f"Você desitiui.\nO número era {numeroObjetivo}.")
        break
    elif (numeroObjetivo == numeroDigitado):
        print("Parabéns! O número era", numeroObjetivo)
        print(f"Voce acertou em {tentativas} tentativas.")
        break
    elif (numeroObjetivo > numeroDigitado):
        print("O número objetivo é maior que", numeroDigitado)
    else:
        print("O número objetivo é menor que", numeroDigitado)