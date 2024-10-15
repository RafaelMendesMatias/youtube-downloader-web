from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=a6991rC2DgA&list=RDa6991rC2DgA&start_radio=1"
 
yt = YouTube(url, on_progress_callback = on_progress)

# print(yt.streams)


for stream in yt.streams:
    if stream.type == "video" and hasattr(stream, "res"):
        print(f"Resolução: {stream.res}, Codec de vídeo: {stream.vcodec}, Codec de áudio: {stream.acodec}")