"""receba um valor monetário em reais brasileiros do usuário
exiba o valor equivalente nas moedas de reais brasileiros, dólar americano e euro europeu.

https://wise.com/br/currency-converter/ 
https://www.bcb.gov.br/conversao """

# Importar as bibliotecas necessarias.
import os
import customtkinter
from tkinter import messagebox

os.system('cls || clear') # limpar tela do terminal.

def converterMoedas():
    # Coletar valor digitado pelo usuario.
    RealBrasileiro = float(RealBrasileiro.get())
    
    # https://www.bcb.gov.br/conversao 
    # Converter para dolar americano.
    dolarAmericano : float = (RealBrasileiro * 0.1758)
    
    # Converter para Euro europeu.
    euroEuropeu : float = (RealBrasileiro * 0.1549)
    
    # exiba o valor equivalente em reais brasileiros, dólar americano e euro europeu.
    messagebox.showinfo("Moedas convertidas",
                        f" Valor em Reais brasileiros: {round (RealBrasileiro, 2)}\n Valor em Dólar Americano: {round(dolarAmericano, 2)}\n Valor em Euro Europeu: {round(euroEuropeu,2)}")
    # valorEquivalenteReais = customtkinter.CTkLabel(janelaPrincipal, 400, 35, text=(""), font=("Arial", 17))

customtkinter.set_appearance_mode("light")
janelaPrincipal = customtkinter.CTk()
janelaPrincipal.title("2º Exercício - Interface: Convertor de moedas")
janelaPrincipal.geometry("480x250")
janelaPrincipal.resizable(False, False)

customtkinter.CTkLabel(janelaPrincipal,
                       text_color=("black"),
                       text=("Convertor de Moedas"),
                       font=("Arial", 25, "bold")).pack(pady = 15)

customtkinter.CTkLabel(janelaPrincipal,
                       text_color=("black"),
                       text=("Valor monetário:"),
                       font=("Arial", 18)).place(x=15,y=70)

# Receber valor monetártio em reais brasileiros.
valorDigitado = customtkinter.CTkEntry(janelaPrincipal, 300, 35,
                                       border_color=("dark blue"),

                                       placeholder_text=("Digite o valor em Reais Brasileiros."),
                                       font=("Roboto", 16))
valorDigitado.place(x=150, y = 67)

# Botão para fazer a conversão.
botaoConverterMoedas = customtkinter.CTkButton(janelaPrincipal, 155, 40,
                                               border_width=(2),
                                               border_color=("dark gray"),
                                               
                                               text=("Converter Moedas"),
                                               font=("Roboto", 17),
                                               
                                               command=converterMoedas)
botaoConverterMoedas.pack(pady=70)

janelaPrincipal.mainloop() # Ativa função da janela Principal.

print("\tTarefa Conluída!")