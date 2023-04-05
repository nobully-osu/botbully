import super_secret

txtFile = super_secret.txtFilePath

def getCurrentSong():
    f = open(txtFile)
    link = f.read()
    f.close()
    return link