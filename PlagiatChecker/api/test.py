from glob import iglob
import os
for fichier in iglob("../media/public/*.pdf"):
    if os.path.isfile(fichier):
        print(fichier)
