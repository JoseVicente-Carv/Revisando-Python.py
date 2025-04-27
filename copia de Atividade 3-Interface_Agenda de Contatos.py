""" Componente: José Vicente Carvalho dos Santos; Turmma 91165, Curso técnico em Desenvolvimento de Sistemas (3º Módulo)
Materia: internet das Coisas    Data: 24/04/2025 """


import os
import customtkinter as interface
from tkinter import *
from tkinter import messagebox

os.system('cls || clear') # limpar tela do termial.

# Defiir funções necessarias.
def salvarAgenda(): # salvar Agenda num docdetexto.
    with open("Registros da agenda.txt", "w") as banco:
        contatosRegistrados = agenda.get(0, END)

        for x in contatosRegistrados:
            banco.write(x + "\n")

    agenda.configure(agenda, width=0) # redefine a largura/width da listBox para caber perfeitamente tds os itens armazenados nela.

def carregarAgenda():
    with open("Registros da agenda.txt", "r") as banco:
        contatosRegistrados = banco.readlines()
        # contatosRegistrados.reverse()

        for a in contatosRegistrados:
            agenda.insert(0, a.strip())
            
        agenda.configure(agenda, width=0) # redefine a largura/width da listBox para caber perfeitamente a tds os itens armazenados nela.

def adicionarContato():
    contato : str = nome.get() + " - " + telefone.get() + " - " + email.get()

    if ((nome.get()) and (telefone.get()) and (email.get())):
        agenda.insert(END, contato) # Insere tarefa escrita pelo usuário na ListBox.
        
        nome.delete(0, END)
        telefone.delete(0, END)
        email.delete(0, END)

        salvarAgenda()
    else:
        messagebox.showerror("Erro em entradas", "Um dos campos do contato está vazio.")

def deletarContato():
    contatoSelecionado = agenda.curselection()

    if (contatoSelecionado):
        agenda.delete(contatoSelecionado)

        salvarAgenda()
    else:
        messagebox.showerror("Erro em deletar contato", "Nenhum contato foi selecionado.")

# Criar janela principal
interface.set_appearance_mode("dark")
janelaAgendaContatos = interface.CTk()
janelaAgendaContatos.title("3ª Atividade - Interface: Agenda de Contatos") # definir nome da janela.
janelaAgendaContatos.geometry("600x450") # definir dimensões da janela em pixels.
janelaAgendaContatos.resizable(False, False) # lacrar as dimensões da janela.

# Pedir nome ao usuario.
nome = interface.CTkEntry(janelaAgendaContatos, 250,35,
                          placeholder_text=("Digite aqui nome."),
                          font=("Roboto", 16))
nome.pack(pady = 10) # Ativar função.

# Pedir telefone ao usuário.
telefone = interface.CTkEntry(janelaAgendaContatos, 250,35,
                              placeholder_text=("Digite aqui telefone."),
                              font=("Roboto", 16))
telefone.pack(pady = 10) # Ativar função.

# Pedir e-mail ao usuário.
email = interface.CTkEntry(janelaAgendaContatos, 250,35,
                           placeholder_text=("Digite aqui e-mail."),
                           font=("Roboto", 16))
email.pack(pady = 10) # Ativar função.

# Exibir Listbox interativa.
agenda = Listbox(janelaAgendaContatos, width=50, background=("#212121"),
                 font=("Arial",12),
                 fg=("white"))
agenda.pack(pady=10)

# Exibir botão para adicionar contato.
botaoAdicionarContato = interface.CTkButton(janelaAgendaContatos, 155, 40,
                                            text=("Adicionar"),
                                            font=("Roboto",17),
                                            cursor=("hand2"),
                                            command=adicionarContato)
botaoAdicionarContato.pack(pady = 10)

# Exibir botão para exlucir contato.
BotaoDeletarContato = interface.CTkButton(janelaAgendaContatos, 155, 40,
                                          text=("Excluir"),
                                          font=("Roboto",17),
                                          command=deletarContato)
BotaoDeletarContato.pack(pady = 10)

carregarAgenda() # carregar contatos do banco de dados na ListBox.

janelaAgendaContatos.mainloop()