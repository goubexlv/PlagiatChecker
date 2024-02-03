from glob import iglob
import os

def Typefile(f):
    ref_file=f
    extension=ref_file.split('.')[-1]
    return extension

def upload_file(f):
    with open('./media/public/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
            
def listedefichier():
    fichiers = []
    for fichier in iglob('./media/public/*.pdf'):
        fichiers.append(str(fichier))
            
    return fichiers

def listedefichiers(tp):
    fichiers = []

    for fichier in iglob('./media/public/*.'+tp):
        fichiers.append(str(fichier))
            
    return fichiers



