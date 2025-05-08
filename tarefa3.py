import tkinter as tk 

def sair():
    janela.destroy()

def cadastro ():
    import login
    subprocess.Popen(["python", "login.py"])

def sistema():
    import sistema
    subprocess.Popen(["python", "sistema.py"])


janela= tk.Tk()
janela.geometry("1920x1080")
janela.config(bg="black")
janela.title("cadastro")

label_contador = tk.Label(janela, text="Faça seu cadastro",font=("Arial", 40))
label_contador.pack(pady=20)

label_contador = tk.Label(janela, text="Seu nome:", font=("Arial", 20))
label_contador.pack(pady=20)

caixa_nome = tk.Entry(janela) 
caixa_nome.pack(pady=20)

label_contador = tk.Label(janela, text="Sua senha:", font=("Arial", 20))
label_contador.pack(pady=20)

caixa_senha = tk.Entry(janela) 
caixa_senha.pack(pady=20)

botao_entrar = tk.Button(janela, text ="Cadastrar", command=cadastro, font=("Arial",20))
botao_entrar.pack(pady=20)

botao_sair= tk.Button(janela, text ="Sair", command = sair, width=10, font="Arial,20")
botao_sair.pack(side="left", pady=10)

botao_sistema= tk.Button(janela, text ="Sobre o sist..", command=sistema, width=10, font="Arial,30")
botao_sistema.pack(side="left", pady=10)

janela.mainloop()