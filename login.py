import tkinter as tk

def sair():
    janela.destroy()

def antivirus ():
    import antivirus
    subprocess.Popen(["python", "antivirus.py"])

janela = tk.Tk()
janela.geometry("1920x1080")
janela.config(bg="black")
janela.title("Cadastro")


label_perfil = tk.Label(janela, text="Seu perfil", font=("Arial", 40)) 
label_perfil.pack(pady=20)


label_nome = tk.Label(janela, text="Nome da pessoa", font=("Arial", 20))  
label_nome.pack(pady=20)

label_senha = tk.Label(janela, text="Senha criptografada", font=("Arial", 20)) 
label_senha.pack(pady=20)


botao_anti_virus = tk.Button(janela, text="Anti Virus",command=antivirus, font=("Arial", 14))
botao_anti_virus.pack(pady=20)


botao_sair= tk.Button(janela, text ="Sair", command = sair, width=10, font="Arial,20")
botao_sair.pack(side="left", pady=10)

janela.mainloop()