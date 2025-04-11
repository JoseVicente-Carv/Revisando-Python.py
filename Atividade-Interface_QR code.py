""" Componente: José Vicente Carvalho dos Santos; Turmma 91165, Curso técnico em Desenvolvimento de Sistemas (3º Módulo)
Materia: internet das Coisas    Data: 10/04/2025 """

# importar biblioteca necessaria.
import os
import customtkinter as interface
import qrcode

# definior funções necessarias.
def gerarQRcode():
    conteudo = textoDigitado.get() # Coletar texto digitado pelo usuario.

    qrCodeGerado = qrcode.make(conteudo) # inserir conteudo digitado num QR Code.
    qrCodeGerado.save("Seu novo QR Code.png") # Salvar novo QR Code como arquivo.

os.system('cls || clear') # limpar tela do termial.

# criar & configurar janela do aplicativo como variável.
interface.set_appearance_mode('dark')

janela = interface.CTk()
janela.title("Interface de QR Code -José Vicente") # definir nome da janela.
janela.geometry("600x450") # definir dimensões da janela em pixels.
janela.resizable(True, True) # lacrar as dimensões da janela.

# Exibir titulo no topo da janela.
interface.CTkLabel(janela, text=("Gerador de QR Code Personalizado"),
                   font=("Roboto", 25)).pack(pady = 10)

# exibir barra para usuario inserir texto/conteudo do codigo qr.
textoDigitado = interface.CTkEntry(janela, 400, 40,
                                   placeholder_text=("Digite a URL."),
                                   font=("caliber", 16))
textoDigitado.place(x=20, y=65)

# Exibir botão para gerar o QR Codigo.
botaoGerar = interface.CTkButton (janela, 100, 40,
                                  text=("Gerar"),
                                  font=("arial", 16, "bold"),
                                  command=gerarQRcode)
botaoGerar.place(x=425, y=65) # ativar função e posicionar botão na janela.

# exibir código QR gerado na janela.
# ¯\(;_;)/¯

janela.mainloop() # Ativar função da janela.
