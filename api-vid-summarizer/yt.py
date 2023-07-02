from pytube import YouTube
from model import *
from summarize_youtube import *
def yt_model(youtubeLink):
    print(youtubeLink)
    VIDEO_URL = youtubeLink
    res = ""
    try:
        res = summarize_youtube_model(youtubeLink)
    except:
        yt = YouTube(VIDEO_URL)
        yt.streams.filter(only_audio = True, file_extension = 'mp4').first().download(filename = './test_docs/video.mp4') 
        res = summarize_text_model(youtubeLink)
    return res