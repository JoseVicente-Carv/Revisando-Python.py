import customtkinter as ctk
from tkinter import *
from tkinter import messagebox

#==============================Funções
def add_tarefa():
    t = tarefa.get()
    if (t):
        lista_tarefa.insert(0,t)
        tarefa.delete(0,END)
        salvar_tarefa()
    else:
        messagebox.showerror('Erro','Campo Vazio!')
     
     
   
def del_tarefa():
    selecionada = lista_tarefa.curselection()
    if (selecionada):
        lista_tarefa.delete(selecionada)
        salvar_tarefa()
    else: 
        messagebox.showerror('Erro', 'Selecione uma Tareja!')
    

def salvar_tarefa():
    with open('tarefa.txt','w') as ta:
        tarefas = lista_tarefa.get(0,END)
        for x in tarefas: 
            ta.write(x+'\n')
            
            
def carregar_tarefa():
    with open('tarefa.txt','r') as ta:
        tarefas = ta.readlines()
        tarefas.reverse()
        for x in tarefas:
            lista_tarefa.insert(0,x.strip())
        
        
        
        
#==============================Janela
ctk.set_appearance_mode('dark')
janela = ctk.CTk()
janela.geometry('350x500')
janela.title('Lista de Tarefas - V1')
janela.resizable(False,False)
#==============================Janela


tarefa = ctk.CTkEntry(janela,
                      width=320,
                      height=40,
                      border_color='hotpink',
                      placeholder_text='Digite a tarefa a ser criada: ')

tarefa.pack(pady=10)



buttonadc = ctk.CTkButton(janela,
                          width=100,
                          height=40,
                          fg_color='lightgreen',
                          hover_color='darkgreen',
                          text='Adicionar Tarefa ',
                          font=('verdana',15,'bold'),
                          cursor='hand2',
                          text_color='black',
                          command= add_tarefa)
buttonadc.place(x=15,y=95)




buttonexcluir = ctk.CTkButton(janela,
                          width=100,
                          height=40,
                          fg_color='red',
                          hover_color='darkred',
                          text='Excluir Tarefa ',
                          font=('verdana',15,'bold'),
                          cursor='hand2',
                          text_color='white',
                          command= del_tarefa)
buttonexcluir.place(x=195,y=95)





lista_tarefa = Listbox(janela,
                       width=30,
                       height=16,
                       font=('verdana',12,'bold'),
                       background='#363636',
                       highlightbackground='hotpink',
                       highlightthickness=2,
                       fg='white')
lista_tarefa.place (x=10,y=180)




carregar_tarefa()
janela.mainloop()