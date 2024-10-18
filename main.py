import sys
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = sys.argv[1]

try:
    yt = YouTube(url, on_progress_callback=on_progress)
    yt = yt.streams.get_highest_resolution()
    yt = vars(yt)
    yt = yt['url']
    print(yt)  # Exibe a URL do áudio
except Exception as e:
    print(f"Erro: {e}")