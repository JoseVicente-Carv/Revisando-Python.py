""" José Vicente Carvalho dos Santos; Turmma 91165, Curso técnico em Desenvolvimento de Sistemas (3º Módulo)
Materia: internet das Coisas    Data: 03/04/2025 """

""" Implemente um programa em Python que:
1.  Leia o nome do aluno.
2.  Utilize uma função para receber e armazenar os três pesos levantados em um vetor, 
    calcular a média dos pesos levantados 
3.  Mostre os resultados do calculo de média na Interface 
    e exibir a mensagem motivacional apropriada na Interface. """


# importe as bibliotecas necessarias
import os
import customtkinter as interface

# Definir as funções necessarias.
def calcularMedia ():
    # iniciar o vetor necessario.
    pesos = []

    # inicar as variaveis necessrias
    p1 = float(primeiroPeso.get())
    p2 = float(segundoPeso.get())
    p3 = float(terceiroPeso.get())

    # Armazene os valores dos pesos no vetor.
    pesos.append(p1)
    pesos.append(p2)
    pesos.append(p3)

    # calcular Média aritmética dos pesos levantados.
    media = sum(pesos) / len(pesos)

    # Exibir resultado do calculo de Média aritmética.
    resultadoMédia.configure(text = f"A média dos pesos levantados: {round(media,2)}")

    # exibir a mensagem motivacional de acordo com o valor da média dos pesos.
    # Se a média for menor que 40 kg, exibir: "Continue firme! O importante é a constância!"
    if (media < 40):
        mensagemMotivacional.configure(text = "Continue firme! O importante é a constância!")
    # Se a média for maior que 80 kg, exibir: "Incrível! Seu desempenho está excelente!"
    elif (media > 80):
        mensagemMotivacional.configure(text = "Incrível! Seu desempenho está excelente!")
    # Se a média for entre 40 kg e 80 kg (inclusive), exibir: "Ótimo trabalho! Você está evoluindo bem!"
    else:
        mensagemMotivacional.configure(text = "Ótimo trabalho! Você está evoluindo bem!")

os.system("cls || clear") # limpar tela do terminal.

# inciar + configurar variavel da janela.
janela = interface.CTk()
interface.set_appearance_mode("dark")

janela.title("Questão 1 - 1ª Avaliação -Internet das Coisas")
janela.iconbitmap("1ª Avaliação -Internet das Coisas/sport_bag_dumbbell_gym_sport_icon.ico")
janela.geometry("600x550")
janela.resizable(False, False)

# Criar titulos no topo da interface.
interface.CTkLabel(janela, text=("Academia Senai Dendezeiros"),
                   text_color=("white"),
                   font=("Arial", 20)).pack(pady = 10)

interface.CTkLabel(janela, text=("Acompanhamento de Progresso"),
                   text_color=("white"),
                   font=("Arial", 30)).pack(pady = 0)

# Criar entrada para nome do cliente/aluno.
nomeAluno = interface.CTkEntry (janela, 300, 40,
                                placeholder_text=("Digite o nome do aluno."),
                                font=("Arial", 17))
nomeAluno.pack(pady = 10) # ativar "função."

# Criar entradas para os 3 pesos levantados pelo aluno.
primeiroPeso = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor do 1º peso em Kg."),
                                   font=("Arial", 17))
primeiroPeso.pack(pady = 10)

segundoPeso = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor do 2º peso em Kg."),
                                   font=("Arial", 17))
segundoPeso.pack(pady = 10)

terceiroPeso = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor do 3º peso em Kg."),
                                   font=("Arial", 17))
terceiroPeso.pack(pady = 10)

# Criar botão para calcular os pesos.
botaoCalcular = interface.CTkButton (janela, 150, 50, 
                                     text=("Calcular média"),
                                     font=("Arial", 17, "bold"),
                                     command=calcularMedia)
botaoCalcular.pack(pady = 30) # ativar "função" do batão.

# Exibir resultado da média.
resultadoMédia = interface.CTkLabel (janela, text=(""),
                                     font=("caliber", 18))
resultadoMédia.pack() # ativar "função".

# Exibir "mensagem motivacional."
mensagemMotivacional = interface.CTkLabel (janela, text=(""),
                                           font=("caliber", 18))
mensagemMotivacional.pack(pady = 20) # ativar "função".

janela.mainloop() # ativar "função" da janela.