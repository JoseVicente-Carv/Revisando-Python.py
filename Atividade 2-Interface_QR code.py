""" Componente: José Vicente Carvalho dos Santos; Turmma 91165, Curso técnico em Desenvolvimento de Sistemas (3º Módulo)
Materia: internet das Coisas    Data: 10/04/2025 """

""" Sobre gerar qr Code:
https://www.youtube.com/watch?v=2yTlvPSIePs
https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d
https://www.devponto.com/posts/como-gerar-qr-code-usando-python/
https://www.tabnews.com.br/Bassani/gerando-qr-codes-com-python-um-guia-ratico-simples-com-exemplos
https://pypi.org/project/qrcode/
https://www.google.com/search?q=biblioteca+python+qrcode+pip+install&oq=biblioteca+python+qrcode+PIP+insta&gs_lcrp=EgZjaHJvbWUqCQgBECEYChigATIGCAAQRRg5MgkIARAhGAoYoAEyCQgCECEYChigATIJCAMQIRgKGKAB0gEJMjM5MjdqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8 """

""" Para exibir imagens:
https://www.pythontutorial.net/tkinter/tkinter-photoimage/
https://www.tcl-lang.org/man/tcl8.6/TkCmd/image.htm
https://tkinter.com/images-in-customtkinter-tkinter-customtkinter-17/ """

""" Fatores a mlehorar: Fazer a imagem atualizar toda vez q o botão "gerar" for pressionado. Atualmente para gerar um novo codigo precisa fechar e abrir a janela. """
# importar biblioteca necessaria.
import os
import customtkinter as interface
import qrcode
from PIL import Image

# definior funções necessarias.
def gerarQRcode():
    conteudo = textoDigitado.get() # Coletar texto digitado pelo usuario.

    qrCodeGerado = qrcode.make(conteudo) # inserir conteudo digitado num QR Code.
    qrCodeGerado.save("Seu novo QR Code.png") # Salvar novo QR Code como arquivo.

    # exibir código QR gerado na janela.
    imagemExibida = interface.CTkImage(Image.open("Seu novo QR Code.png"),
                                       Image.open("Seu novo QR Code.png"),
                                       (400, 400))
    
    frameImagem = interface.CTkLabel(janela, text=(""), image=imagemExibida)
    frameImagem.pack(pady=100)

os.system('cls || clear') # limpar tela do termial.

# criar & configurar janela do aplicativo como variável.
interface.set_appearance_mode('dark')

janela = interface.CTk()
janela.title("Interface de QR Code -José Vicente") # definir nome da janela.
janela.geometry("550x650") # definir dimensões da janela em pixels.
janela.resizable(False, False) # Permitir que o usuário mude as dimensões da janela.

# Exibir titulo no topo da janela.
interface.CTkLabel(janela,
                   text=("Gerador de QR Code Personalizado"),
                   font=("Roboto", 25)).pack(pady = 10)

# exibir barra para usuario inserir texto/conteudo do codigo qr.
textoDigitado = interface.CTkEntry(janela, 400, 40,
                                   placeholder_text=("Digite uma URL."),
                                   font=("caliber", 16))
textoDigitado.place(x=20, y=65)

# Exibir botão para gerar o Codigo QR.
botaoGerar = interface.CTkButton (janela, 100, 40,
                                  text=("Gerar"),
                                  font=("arial", 16, "bold"),
                                  command=gerarQRcode)
botaoGerar.place(x=425, y=65) # ativar função e posicionar botão na janela.

janela.mainloop() # Ativar função da janela.