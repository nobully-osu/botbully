import os

textfile = "C:\\Users\\Matthew\\Desktop\\Games\\osuStreamCompanion\\Files\\np_playing_DL.txt"

#f = open(textfile)
#link = f.read()
#f.close()

#with open(textfile) as f:
#   link = f.read()

def getCurrentSong():
    f = open(textfile)
    link = f.read()
    f.close()
    return link