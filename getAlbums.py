# ------------
# getAlbums.py
# ------------
#
# Получение списка альбомов исполнителя по его ID в MusicBrainz 
# запуск:  
#              python3 getAlbum.py artist-ID
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

def getAlbumList(artist):

    #result = musicbrainzngs.search_releases(artist=artist, release=album, limit=10)
    result = musicbrainzngs.search_releases(arid=artist, limit=None, strict=True)

    for rel in result['release-list']:
       id = rel["id"]    
       new_result = musicbrainzngs.get_release_by_id(id, includes=["recordings"])

       print(new_result['release']['title'])
       if 'date' in new_result['release']:
          print(new_result['release']['date'])
       if 'format' in  new_result['release']['medium-list'][0]:  
          print(new_result['release']['medium-list'][0]['format'])
       print()           

if __name__ == '__main__':
    if len(sys.argv) > 0:
        artist = sys.argv[1]
        getAlbumList(artist)
    else:
        print("Artist ID is missing")
    