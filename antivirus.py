import tkinter as tk

def sair():
    janela.destroy()

def alternar_estado():
    global ativado
    ativado = not ativado
    if ativado:
        botao.config(text="Desativar anti virus")
        label_perfil.config(text="Antivirús ativado")
    else:
        botao.config(text="Ativar anti virus")
        label_perfil.config(text="Antivírus desativado")

janela = tk.Tk()
janela.geometry("1920x1080")
janela.config(bg="black")
janela.title("antivirus")

ativado = True


label_perfil= tk.Label(janela, text = antivirus, font=("Arial", 20))
label_perfil.pack(pady=20)

botao = tk.Button(janela, text="Desativar anti virus", font=("Arial", 20), command=alternar_estado)
botao.pack(pady=10)

botao_sair= tk.Button(janela, text ="Sair", command = sair, width=10, font="Arial,20")
botao_sair.pack(side="left", pady=10)

janela.mainloop()