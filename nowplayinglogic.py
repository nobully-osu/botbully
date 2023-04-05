import os

textfile = "C:\\Users\\Matthew\\Desktop\\Games\\osuStreamCompanion\\Files\\np_playing_DL.txt"

def getCurrentSong():
    f = open(textfile)
    link = f.read()
    f.close()
    return link