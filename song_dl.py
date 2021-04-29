import youtube_dl
import sys
from youtubesearchpython import VideosSearch

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '/Users/edoardo/Desktop/songDW/songs/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

def search_songs(titles):
    urls = []
    for title in titles:
        videosSearch = VideosSearch(title, limit = 1)
        results = videosSearch.result()
        url = results.get('result')[0].get('link')
        urls.append(url)
    return urls

def download_songs(urls):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(urls)

def load_songs_from_file():
    songs = []
    try:
        f = open('./songs.txt', 'r')
        while f:
            song = f.readline()
            song = song.rstrip()
            if song == "":
                break
            songs.append(song)
        f.close()
        return songs
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    songs = load_songs_from_file()
    download_songs(search_songs(songs))
