import customtkinter
from CONECTOR import conexao

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("500x300")

def autenticar_login():
    conn = conexao.conectar_banco()
    cursor = conn.cursor()

    user_valor = admin.get()
    senha_valor = senha.get()

    cursor.execute("SELECT * FROM usuario WHERE username = %s AND senha = %s", (user_valor, senha_valor))
    usuario = cursor.fetchone()

    conn.close()

    if usuario:
        print("Login bem-sucedido!")
    else:
        print("Erro: Login ou senha incorretos.")


texto = customtkinter.CTkLabel(janela, text="GERENCIADOR DE AVISOS")
admin = customtkinter.CTkEntry(janela, placeholder_text="Admin")
senha = customtkinter.CTkEntry(janela, placeholder_text="Senha", show="*")
botao = customtkinter.CTkButton(janela, text="Entrar", command=autenticar_login)

texto.pack(padx=10, pady=10)
admin.pack(padx=10, pady=10)
senha.pack(padx=10, pady=10)
botao.pack(padx=10, pady=10)

janela.mainloop()