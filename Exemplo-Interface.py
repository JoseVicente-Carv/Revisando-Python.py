import customtkinter as ctk

ctk.set_appearance_mode('dark')

janela = ctk.CTk('#073')
# janela = ctk.CTk('magenta')
janela.geometry('600x500')

janela.resizable(False,True)

janela.title('Janela de Vicente')

ctk.CTkLabel(janela, text="Sistema de acesso", 
             font=('Arial',35,"italic"),
             text_color="yellow").pack(pady=20)

login = ctk.CTkEntry(janela,width=400,height=40,
                     placeholder_text="Digite aqui seu login.",
                     font=('Arial', 20))
login.pack()

senha = ctk.CTkEntry(janela, 
                     width=400,
                     height= 40,
                     placeholder_text=("Digite aqui sua senha."),
                     show="*")
senha.pack(pady=10)

botao = ctk.CTkButton(janela,width=150,height=40,
                      fg_color="white",
                      text="Verificar",
                      text_color="black", font=("arial", 18, "bold"),
                      hover_color="yellow")
botao.pack(pady=15)

janela.mainloop()
