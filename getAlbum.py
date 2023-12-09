# -----------
# getAlbum.py
# -----------
#
# Получение списка альбомов исполнителя по его ID в MusicBrainz 
# запуск:  
#              python3 getAlbum.py artist-ID album-name
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

def getTrackList(artist, album):

    #result = musicbrainzngs.search_releases(artist=artist, release=album, limit=10)
    result = musicbrainzngs.search_releases(arid=artist, release=album, limit=None, strict=True)

    for rel in result['release-list']:
       id = rel["id"]    
       new_result = musicbrainzngs.get_release_by_id(id, includes=["recordings"])

       print(new_result['release']['title'])
       if 'date' in new_result['release']:
          print(new_result['release']['date'])

       if 'format' in  new_result['release']['medium-list'][0]:  
          print(new_result['release']['medium-list'][0]['format'])
       print()

       t = (new_result["release"]["medium-list"][0]["track-list"])


       for x in range(len(t)):
          line = (t[x])

          if 'length' in line:
             length = int(line['length'])//1000
             mins = length // 60
             secs = length % 60
             left = f'{line["number"]}. {line["recording"]["title"]}'
             right = f'{mins:02d}:{secs:02d}'
             print('{}{}'.format(left.ljust(50),right))
          else:
             print(f'{line["number"]}. {line["recording"]["title"]}')
       print()  
          

if __name__ == '__main__':
    if len(sys.argv) > 1:
        artist, album = [sys.argv[1], sys.argv[2]]
        getTrackList(artist, album)
    else:
        print("Artist or Album missing")
    