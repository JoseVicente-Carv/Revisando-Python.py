""" 6) Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato e quem ganhou a eleição. """

import os

# inicie as variaveis necessarias
candidato1 : int = 0
candidato2 : int = 0
candidato3 : int = 0
votoNulo   : int = 0

# Faça um programa que peça o número total de eleitores. 
os.system("cls || clear")
quantidadeEleitores = int(input("Quantidade de eleitores: "))

# colete o voto de cada eleitor
for contador in range(quantidadeEleitores):
    # os.system("cls || clear")
    voto = int(input(f"{contador+1}. Digite o seu voto (1-3): ")) # colete o voto do eleitor

    # conte o voto pro candidato respectivo
    if (voto == 1):
        candidato1 += 1
    elif (voto == 2):
        candidato2 += 1
    elif (voto == 3):
        candidato3 += 1
    else:
        votoNulo += 1

# exibir os resultados da eleição
# os.system("cls || clear")
print(f"\tResultados da eleição:")
print(f"Candidato 1: {candidato1} votos.")
print(f"Candidato 2: {candidato2} votos.")
print(f"Candidato 3: {candidato3} votos.")
print(f"Votos nulos: {votoNulo}\n")

if (candidato1 > candidato2 and candidato1 > candidato2):
    print(f"O candidato 1 venceu a eleição.")
elif (candidato2 > candidato1 and candidato2 > candidato3):
    print(f"O candidato 2 venceu a eleição.")
elif (candidato3 > candidato1 and candidato3 > candidato2):
    print(f"O candidato 3 venceu a eleição.")