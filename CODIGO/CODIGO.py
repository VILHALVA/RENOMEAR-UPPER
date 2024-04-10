import os
import tkinter as tk
from tkinter import filedialog

def renomear_arquivos(diretorio):
    try:
        arquivos = os.listdir(diretorio)
        for arquivo in arquivos:
            if os.path.isfile(os.path.join(diretorio, arquivo)):
                nome_arquivo, extensao = os.path.splitext(arquivo)
                nome_arquivo_upper = nome_arquivo.replace(" ", "_").upper()
                novo_nome = f"{nome_arquivo_upper}{extensao}"
                os.rename(os.path.join(diretorio, arquivo), os.path.join(diretorio, novo_nome))

        mensagem.config(text="Arquivos renomeados com sucesso para maiúsculas!")

    except Exception as e:
        mensagem.config(text=f"Ocorreu um erro: {str(e)}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        renomear_arquivos(diretorio)

janela = tk.Tk()
janela.title("RENOMEAR PARA UPPER")

footer_label = tk.Label(janela, text="APP CRIADO PELO VILHALVA\nGITHUB: @VILHALVA", bg="gray", fg="white", height=2)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)        
janela.state('zoomed')

selecionar_botao = tk.Button(janela, text="SELECIONAR", command=selecionar_diretorio)
selecionar_botao.pack(pady=20)

mensagem = tk.Label(janela, text="", fg="green")
mensagem.pack()

janela.mainloop()
