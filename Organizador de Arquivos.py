import os
import shutil

# Mapeamento de extensões para nomes de pastas
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

# Caminho do diretório atual
diretorio_atual = os.getcwd()

# Função para encontrar o tipo de arquivo com base na extensão
def encontrar_tipo(extensao):
    for tipo, extensoes in tipos_arquivo.items():
        if extensao.lower() in extensoes:
            return tipo
    return "Outros"

# Organiza os arquivos
for item in os.listdir(diretorio_atual):
    caminho_completo = os.path.join(diretorio_atual, item)
    
    # Ignora pastas
    if os.path.isdir(caminho_completo):
        continue

    # Pega a extensão do arquivo
    _, extensao = os.path.splitext(item)
    
    # Descobre a pasta de destino
    tipo = encontrar_tipo(extensao)
    pasta_destino = os.path.join(diretorio_atual, tipo)
    
    # Cria a pasta se não existir
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
    
    # Move o arquivo
    shutil.move(caminho_completo, os.path.join(pasta_destino, item))
    print(f"Movido: {item} -> {tipo}/")

print("\nOrganização concluída com sucesso!")