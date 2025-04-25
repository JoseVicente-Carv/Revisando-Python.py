""" Componente: José Vicente Carvalho dos Santos; Turmma 91165, Curso técnico em Desenvolvimento de Sistemas (3º Módulo)
Materia: internet das Coisas    Data: 24/04/2025 """

""" https://keep.google.com/#NOTE/1LJ-uQJd1U5CVKuYm6JnOo88aOIxidS-pGVKS3ccSxux-7-Fw0dyhK_vAtOfMfxg
https://photos.google.com/share/AF1QipOtHJ2zEf28dvnA-86XRSDnRk1GsZH4cHxzCI_cvh2EkXw2QV8yReTnvtrU7Ra2Zg/photo/AF1QipMh6J7H_I_EeiY_8d8sxSAEb3coAGEpM6gYx4f9
https://www.google.com/search?q=ctk+imagery&oq=ctk+imager&gs_lcrp=EgZjaHJvbWUqBwgBECEYoAEyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigAdIBCDQ4MTVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
https://www.tcl-lang.org/man/tcl8.6/TkCmd/listbox.htm#M11
https://awari.com.br/funcao-len-python-como-usar-a-funcao-len-para-contar-caracteres-em-python/ """


import os
import customtkinter as interface
from tkinter import *
from tkinter import messagebox

os.system('cls || clear') # limpar tela do termial.

# Defiir funções necessarias.
def salvarAgenda(): # salvar Agenda num docdetexto.
    with open("Registros da agenda.txt", w) as banco:
        contatosRegistrados = agenda.get(0, END)

        for x in contatosRegistrados:
            banco.write(x + "\n")

    agenda.configure(agenda, width=0) # redefine a largura/width da listBox para caber perfeitamente a tds os itens armazenados nela.
    # Talvel cause problemas se acbar apagando tds os itens nela

def carregarAgenda:
    with open("Registros da agenda.txt", r) as banco:
        contatosRegistrados = banco.readlines()
        # contatosRegistrados.reverse()

        for a in contatosRegistrados:
            agenda.insert(0, a.strip())
            
        agenda.configure(agenda, width=0) # redefine a largura/width da listBox para caber perfeitamente a tds os itens armazenados nela.
        # Talvel cause problemas se acbar apagando tds os itens nela

def adicionarContato():
    contato : str = nome.get() + " - " + telefone.get() + " - " + email.get()
    agenda.insert(END, contato)
    # salvarAgenda() no banco de dados

    print(contato) # mostra as palavras inseridas na ListBox
    print(len(contato)) # Mostra o numeros de caracteres do contato adicionado

def deletarContato():
    contatoSelecionado = agenda.curselection()
    agenda.delete(contatoSelecionado)
    # salvarAgenda() no banco de dados

# Criar janela principal
interface.set_appearance_mode("dark")
janelaAgendaContatos = interface.CTk()
janelaAgendaContatos.title("3ª Atividade - Interface: Agenda de Contatos") # definir nome da janela.
janelaAgendaContatos.geometry("600x450") # definir dimensões da janela em pixels.
janelaAgendaContatos.resizable(True, True) # lacrar as dimensões da janela.

# Pedir nome ao usuario.
nome = interface.CTkEntry(janelaAgendaContatos, 250,35, placeholder_text=("Digite aqui nome."), font=("Roboto", 16))
nome.pack() # Ativar função.

# Pedir telefone ao usuário.
telefone = interface.CTkEntry(janelaAgendaContatos, 250,35, placeholder_text=("Digite aqui telefone."), font=("Roboto", 16))
telefone.pack() # Ativar função.

# Pedir e-mail ao usuário.
email = interface.CTkEntry(janelaAgendaContatos, 250,35, placeholder_text=("Digite aqui e-mail."), font=("Roboto", 16))
email.pack() # Ativar função.

# Exibir Listbox interativa.
agenda = Listbox(janelaAgendaContatos,background=("#212121"), font=("Arial",12), width=50, fg=("white"))
agenda.pack()

# Exibir botão para adicionar contato.
botaoAdicionarContato = interface.CTkButton(janelaAgendaContatos, 155, 40, text=("Adicionar"), font=("Roboto",17),
                                            command=adicionarContato)
botaoAdicionarContato.pack()

# Exibir botão para exlucir contato.
BotaoDeletarContato = interface.CTkButton(janelaAgendaContatos, 155, 40, text=("Excluir"), font=("Roboto",17),
                                     command=deletarContato)
BotaoDeletarContato.pack()

carregarAgenda() # carregar contatos do banco de dados na ListBox.

janelaAgendaContatos.mainloop()
print("\tTarefa Concluída!")