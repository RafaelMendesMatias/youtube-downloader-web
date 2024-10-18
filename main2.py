from pytubefix import YouTube
from pytubefix.cli import on_progress
 
videos = []

while True:
    url = input("INSIRA URL DO VIDEO: ")
    formato = input("1-AUDIO; 2-VIDEO: ")
    yt = YouTube(url, on_progress_callback = on_progress)

    print(yt.title)
    
    ys = yt.streams.get_audio_only()
    ys = vars(ys)
    ys = ys['url']
    print(ys)
    # ys.download(mp3=True)

    videos = []

    while True:
        videos = [
            {"nome": "Video 1", "url": "https://example.com/video1"},
            {"nome": "Video 2", "url": "https://example.com/video2"}
        ]