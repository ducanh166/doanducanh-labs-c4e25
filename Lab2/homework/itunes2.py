from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())
section = soup.find("section", "section chart-grid")
# print(section)

li_list = section.find_all("li")
song_list = []

for li in li_list:
    song_name = li.h3.a.string
    artist = li.h4.a.string
    link = li.h3.a["href"]
    songs = {
        "song name": song_name,
        "artist": artist,
        "link": link
    }
    song_list.append(OrderedDict(songs))

option = {
    "default_search": "ytsearch",
    "max_downlaod": 1
}
dl = YoutubeDL(option)
dl.download([song_name + artist])