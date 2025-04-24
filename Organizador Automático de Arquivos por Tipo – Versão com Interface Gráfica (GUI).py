import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Dicionário com categorias e extensões
tipos_arquivo = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".odt"],
    "Planilhas": [".xls", ".xlsx", ".csv"],
    "Apresentações": [".ppt", ".pptx"],
    "Vídeos": [".mp4", ".mov", ".avi", ".mkv"],
    "Áudios": [".mp3", ".wav", ".aac"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executáveis": [".exe", ".msi"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Outros": []
}

# Função para descobrir tipo de arquivo
def encontrar_tipo(extensao):
    for tipo, extensoes in tipos_arquivo.items():
        if extensao.lower() in extensoes:
            return tipo
    return "Outros"

# Função principal de organização
def organizar_pasta(caminho):
    arquivos_organizados = 0
    for item in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, item)

        if os.path.isdir(caminho_completo):
            continue

        _, extensao = os.path.splitext(item)
        tipo = encontrar_tipo(extensao)
        pasta_destino = os.path.join(caminho, tipo)

        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)

        shutil.move(caminho_completo, os.path.join(pasta_destino, item))
        arquivos_organizados += 1

    return arquivos_organizados

# Interface gráfica
def escolher_diretorio():
    pasta = filedialog.askdirectory(title="Selecione a pasta para organizar")
    if not pasta:
        return

    total = organizar_pasta(pasta)
    messagebox.showinfo("Organização Concluída", f"Total de arquivos organizados: {total}")

# Criar janela principal
janela = tk.Tk()
janela.title("Organizador de Arquivos por Tipo")
janela.geometry("400x200")
janela.resizable(False, False)

# Rótulo
label = tk.Label(janela, text="Clique no botão abaixo para escolher a pasta a ser organizada:",
                 font=("Arial", 10), wraplength=350, justify="center")
label.pack(pady=20)

# Botão
botao = tk.Button(janela, text="Selecionar Pasta", font=("Arial", 12), bg="#4CAF50", fg="white",
                  padx=10, pady=5, command=escolher_diretorio)
botao.pack()

# Rodar a interface
janela.mainloop()