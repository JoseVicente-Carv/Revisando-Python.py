import os

# incie a função necessaria
def calcular(x, y, z): 
    resultado: float = (x / y) * z # formula: (distancia / consumo) * preço

    # devolva o resultado da equação
    return resultado

# receba do usuareio os valores de distancia da viagem (km), consumo do veiculo (L/Km) e preço do combustivel (R$/L).
os.system('cls || clear')
distancia = float(input("Insira a distancia da viagem (em km): "))
consumo = float(input("Insira o consumo de combustivel do veiclulo (em L/km): "))
preco = float(input("Insira o preço do combustivel (R$/L): "))

# calcule o custo da viagem
custo : float = calcular(distancia, consumo, preco)

# exibir o custo da viagem
os.system("cls || clear")
print(f"O custo total da viagem será R${custo:.2f}.") 