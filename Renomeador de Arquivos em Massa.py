import os

def renomear_arquivos(
    pasta,
    prefixo="",
    sufixo="",
    substituir=None,
    nova_palavra="",
    adicionar_numero=False
):
    arquivos = os.listdir(pasta)
    arquivos = [f for f in arquivos if os.path.isfile(os.path.join(pasta, f))]
    arquivos.sort()

    for i, nome_antigo in enumerate(arquivos):
        nome_base, extensao = os.path.splitext(nome_antigo)
        novo_nome = nome_base

        # Substituição
        if substituir and substituir in novo_nome:
            novo_nome = novo_nome.replace(substituir, nova_palavra)

        # Adiciona prefixo/sufixo
        novo_nome = f"{prefixo}{novo_nome}{sufixo}"

        # Numeração
        if adicionar_numero:
            novo_nome = f"{i+1:03d}_{novo_nome}"

        novo_nome_completo = novo_nome + extensao
        caminho_antigo = os.path.join(pasta, nome_antigo)
        caminho_novo = os.path.join(pasta, novo_nome_completo)

        os.rename(caminho_antigo, caminho_novo)
        print(f"✔️  {nome_antigo} → {novo_nome_completo}")

if __name__ == "__main__":
    print("📁 Renomeador de Arquivos em Massa")
    pasta = input("Caminho da pasta com os arquivos: ").strip()
    prefixo = input("Prefixo (opcional): ").strip()
    sufixo = input("Sufixo (opcional): ").strip()
    substituir = input("Texto a substituir (opcional): ").strip() or None
    nova_palavra = ""
    if substituir:
        nova_palavra = input(f"Substituir '{substituir}' por: ").strip()
    adicionar_numero = input("Adicionar numeração sequencial? (s/n): ").lower() == "s"

    renomear_arquivos(pasta, prefixo, sufixo, substituir, nova_palavra, adicionar_numero)