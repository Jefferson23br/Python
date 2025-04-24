from pytube import YouTube
import os

def baixar_video(url, pasta_destino='.'):
    try:
        yt = YouTube(url)
        print(f"\n📹 Título: {yt.title}")
        print(f"👤 Canal: {yt.author}")
        print("⏱️ Duração:", yt.length, "segundos")

        print("\n📥 Resoluções disponíveis:")
        streams = yt.streams.filter(progressive=True, file_extension='mp4')
        for i, stream in enumerate(streams):
            print(f"{i + 1}. {stream.resolution} - {round(stream.filesize / (1024 * 1024), 2)} MB")

        escolha = int(input("\nDigite o número da resolução desejada: ")) - 1
        stream_escolhido = streams[escolha]

        print("\n🔽 Baixando...")
        stream_escolhido.download(output_path=pasta_destino)
        print("✅ Download concluído!")

    except Exception as e:
        print("❌ Ocorreu um erro:", e)

if __name__ == "__main__":
    url = input("Insira a URL do vídeo do YouTube: ").strip()
    destino = input("Pasta de destino (pressione Enter para usar o diretório atual): ").strip() or "."
    baixar_video(url, destino)