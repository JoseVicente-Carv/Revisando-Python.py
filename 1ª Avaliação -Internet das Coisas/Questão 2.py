""" José Vicente Carvalho dos Santos; Turmma 91165, Curso técnico em Desenvolvimento de Sistemas (3º Módulo)
Materia: internet das Coisas    Data: 03/04/2025 """

""" Sistema de Orçamento Financeiro:
Desenvolva um sistema de orçamento financeiro pessoal em uma interface gráfica.

Permita que o usuário insira suas receitas e despesas mensais, 
calcule o saldo final.

No mínimo (4 Receitas e 4 Despesas). """

# importe as bibliotecas necessárias .
import os
import customtkinter as interface

# Definir as funções necessárias.
def calcularSaldo ():
    # inicar as variaveis das receitas.
    r1 = float(primeiraReceita.get())
    r2 = float(segundaReceita.get())
    r3 = float(terceiraReceita.get())
    r4 = float(quartaReceita.get())

    # Inicie as variaveis das despesas.
    d1 = float(primeiraDespesa.get())
    d2 = float(segundaDespesa.get())
    d3 = float(terceiraDespesa.get())
    d4 = float(quartaDespesa.get())

    # calcular saldo final do cliente.
    s = (r1 + r2 + r3 + r4) - (d1+d2+d3+d4)

    # Exibir resultado do calculo do saldo.
    saldo.configure(text = f"O seu saldo final é {round(s,2)}")

os.system("cls || clear") # limpar tela do terminal.

# inciar + configurar variavel da janela.
janela = interface.CTk()
interface.set_appearance_mode("dark")

janela.title("Questão 2 - 1ª Avaliação -Internet das Coisas")
janela.geometry("580x700")
janela.resizable(False, False)

# Criar titulos no topo da interface.
interface.CTkLabel(janela, text=("Banco Senai Dendezeiros"),
                   text_color=("white"),
                   font=("Arial", 20)).pack(pady = 10)

interface.CTkLabel(janela, text=("Orçamento Financeiro"),
                   text_color=("white"),
                   font=("Arial", 30)).pack(pady = 0)

# Criar entradas para as 4 receitas do cliente.
primeiraReceita = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma receita em R$."),
                                   font=("Arial", 17))
primeiraReceita.pack(pady = 10)

segundaReceita = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma receita em R$."),
                                   font=("Arial", 17))
segundaReceita.pack(pady = 10)

terceiraReceita = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma receita em R$."),
                                   font=("Arial", 17))
terceiraReceita.pack(pady = 10)

quartaReceita = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma receita em R$."),
                                   font=("Arial", 17))
quartaReceita.pack(pady = 10)

# Criar entradas para as 4 despesas do cliente.
primeiraDespesa = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma despesa em R$."),
                                   font=("Arial", 17))
primeiraDespesa.pack(pady = 10) # Ativar "função."

segundaDespesa = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma despesa em R$."),
                                   font=("Arial", 17))
segundaDespesa.pack(pady = 10) # Ativar "função."

terceiraDespesa = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma despesa em R$."),
                                   font=("Arial", 17))
terceiraDespesa.pack(pady = 10) # Ativar "função."

quartaDespesa = interface.CTkEntry (janela,300, 40,
                                   placeholder_text=("Digite o valor de uma despesa em R$."),
                                   font=("Arial", 17))
quartaDespesa.pack(pady = 10) # Ativar "função."

# Criar botão para calcular o saldo final.
botaoCalcular = interface.CTkButton (janela, 150, 50, 
                                     text=("Calcular saldo"),
                                     font=("Arial", 17, "bold"),
                                     command=calcularSaldo)
botaoCalcular.pack(pady = 15) # ativar "função" do batão.

# Exibir saldo final.
saldo = interface.CTkLabel (janela, text=(""),
                                     font=("caliber", 18))
saldo.pack(pady = 15) # ativar "função".

janela.mainloop() # ativar "função" da janela.