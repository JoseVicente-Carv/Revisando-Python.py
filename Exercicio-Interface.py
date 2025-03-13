""" 600px de largura & 450px de altura
dimensões não manipuláveis pelo usuário
paleta de cores harmônica """

# importar biblioteca necessaria
import customtkinter

# criar & configurar janela do aplicativo como varaivel ---------------- #
janela = customtkinter.CTk()
# professor fez modo escuro
janela.title("Exercicío-Interface -José Vicente") # definir nome da janela
janela.iconbitmap("car_13260.ico") # mudar iconde da janela 
janela.geometry("600x450") # definir dimensões da janela em pixels
janela.resizable(False, False) # lacrar as dimensões da janela
# ---------------------------------------------------------------------- #

# criar um label no topo da janela
customtkinter.CTkLabel(janela, text="APP Consumo de viagem", font=("roboto", 40)).pack()
# professor fez texto amarelo, fonte verdana 40 em bold

# criar 2º label na janela
customtkinter.CTkLabel(janela, text=("03/2025 - Senai Bahia"), font=("Caliber", 30)).pack()
# professor fez texto amarelo, fonte verdana 25 em bold

# criar entrada para a distancia da viagem
customtkinter.CTkLabel(janela, text=("Distancia: "), 
                       text_color=("yellow"),
                       font=("verdana", 15, "bold")
                       ).place(x = 20, y = 120) # professor fez essas linhas (26-28)

distancia = customtkinter.CTkEntry (janela, 420, 40, 
                                    placeholder_text=("Digite a distância da viagem em Km."), 
                                    font=("Arial", 16))
distancia.pack(pady = 50) # ativar "função"

# criar entrada para o consmo de combustivel do veiculo
consumo = customtkinter.CTkEntry (janela, 420, 40,
                                  placeholder_text=("Digite o consumo de combustivel do veiculo em L/Km."),
                                  font=("Arial", 16))
consumo.pack() # ativar "função"

# criar entrada para o preço do combustivel
preco = customtkinter.CTkEntry (janela, width=420, height=40, 
                                placeholder_text=("Digite aqui o preço do combústivel em L/R$."),
                                font=("Arial", 16))
preco.pack(pady = 10) # ativar "função"

# criar botão para calcular
botao = customtkinter.CTkButton (janela, width=150, height=40, text=("Calcular preço da viagem."))
botao.place(x = 220, y = 370)

janela.mainloop() # ativar janela