# getArtist.py
# -----------
#
# Получение списка исполнителей по названию в MusicBrainz 
# запуск:  
#              python3 getArtist.py artist-name
#

from __future__ import print_function
from __future__ import unicode_literals
import musicbrainzngs
import sys

musicbrainzngs.set_useragent(
    "python-musicbrainzngs-example",
    "0.1",
    "https://github.com/alastair/python-musicbrainzngs/",
)

def getArtistList(artist):
    artists = musicbrainzngs.search_artists(query=artist, limit=None, strict=True)
    for art in artists['artist-list']:       
       if 'country' in art:
         print(art['name'], art['country'], art['id'])
       else:
         print(art['name'], art['id'])

if __name__ == '__main__':
    if len(sys.argv) > 0:
        artist = sys.argv[1]
        getArtistList(artist)
    else:
        print("Artist is missing")
    