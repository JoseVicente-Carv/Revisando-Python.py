# importar biblioteca necessaria
import customtkinter

# criar & configurar janela do aplicativo como varaivel ---------------- #
janela = customtkinter.CTk() # iniciar variavel

customtkinter.set_appearance_mode("dark") # modo escuro
janela.title("Exercicío-Interface -José Vicente") # definir nome da janela
# janela.iconbitmap("car_13260.ico") # mudar iconde da janela 
janela.geometry("600x450") # definir dimensões da janela em pixels
janela.resizable(False, False) # lacrar as dimensões da janela
# ---------------------------------------------------------------------- #

# criar um label no topo da janela
customtkinter.CTkLabel(janela, text_color=("yellow"), text="APP Consumo de viagem", font=("rverdana", 40, "bold")).pack()

# criar 2º label na janela
customtkinter.CTkLabel(janela, text_color=("yellow"), text=("03/2025 - Senai Bahia"), font=("rverdana", 25, "bold")).pack()

# criar entrada para a distancia da viagem
customtkinter.CTkLabel(janela, text=("Distancia: "), 
                       text_color=("yellow"),
                       font=("verdana", 15, "bold")
                       ).place(x = 20, y = 120) 

distancia = customtkinter.CTkEntry (janela, 420, 40, 
                                    placeholder_text=("Digite a distância da viagem em Km."), 
                                    font=("Arial", 16))
distancia.place(x=110, y = 120) # ativar e posicionar "função"

# criar entrada para o consmo de combustivel do veiculo
customtkinter.CTkLabel(janela, text=("Consumo: "), 
                       text_color=("yellow"),
                       font=("verdana", 15, "bold")
                       ).place(x = 20, y = 200) 

consumo = customtkinter.CTkEntry (janela, 420, 40,
                                  placeholder_text=("Digite o consumo de combustivel do veiculo em L/Km."),
                                  font=("Arial", 16))
consumo.place(x=110, y = 200) # ativar e posicionar "função"

# criar entrada para o preço do combustivel
customtkinter.CTkLabel(janela, text=("Preço: "), 
                       text_color=("yellow"),
                       font=("verdana", 15, "bold")
                       ).place(x = 20, y = 280) 

preco = customtkinter.CTkEntry (janela, width=420, height=40, 
                                placeholder_text=("Digite aqui o preço do combústivel em L/R$."),
                                font=("Arial", 16))
preco.place(x=110, y=280) # ativar e posicionar "função"

# criar botão para calcular
botao = customtkinter.CTkButton (janela, width=150, height=40, text=("Calcular preço da viagem."))
botao.place(x = 220, y = 350) # ativar e posicionar "função"

janela.mainloop() # ativar janela