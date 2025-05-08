import tkinter as tk 

janela = tk.Tk()
janela.geometry("1920x1080")
janela.config(bg="white")
janela.title("antivirus")


label_perfil = tk.Label(janela, text="Config do sistema", font=("Arial", 40)) 
label_perfil.pack(pady=20)

label_perfil = tk.Label(janela, text="-", font=("Arial", 40)) 
label_perfil.pack(pady=20)


janela.mainloop()