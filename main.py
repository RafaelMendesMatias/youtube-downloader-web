from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=rV5E-Hca3B4"
yt = YouTube(url, on_progress_callback = on_progress)


 
# yt = yt.streams.get_highest_resolution()
yt = yt.streams.get_audio_only()



yt = vars(yt)
yt = yt['url']
print(yt)
# print(vars(yt))