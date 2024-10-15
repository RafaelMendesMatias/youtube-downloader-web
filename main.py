from pytubefix import YouTube
from pytubefix.cli import on_progress
 
url = "https://www.youtube.com/watch?v=a6991rC2DgA&list=RDa6991rC2DgA&start_radio=1"
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.vid_details)

print(dir(yt))
 
# ys = yt.streams.get_highest_resolution()
# ys.download()