import super_secret

mapLink = super_secret.txtFilePath + 'np_playing_DL.txt'
mapInfo = super_secret.txtFilePath + 'np_all.txt'
mapPP = super_secret.txtFilePath + 'np_pp.txt'

def getSongLink():
    f = open(mapLink)
    link = f.read()
    f.close()
    return link

def getSongInfo():
    g = open(mapInfo)
    info = g.read()
    g.close()
    return info

def getSongPP():
    h = open(mapPP)
    pp = h.read()
    h.close()
    return pp