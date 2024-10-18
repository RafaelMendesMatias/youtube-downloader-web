from pytubefix import YouTube
from pytubefix.cli import on_progress
 
videos = []

while True:
    url = input("INSIRA URL DO VIDEO: ")
    formato = int(input("1-AUDIO; 2-VIDEO: "))
    
    yt = YouTube(url, on_progress_callback = on_progress)
    titulo = yt.title
    
    if formato == 1: # Audio
        ys = yt.streams.get_audio_only()
    elif formato == 2: # Video
        ys = yt.streams.get_highest_resolution()
    else: #Erro
        print("Formato invalido")
        exit()
    
    ys = vars(ys)
    url = ys['url']
    
    # ys.download(mp3=True)

    novo = {"titulo": f"{titulo}", "url": f"{url}"}
    videos.append(novo)
   
    print(videos)