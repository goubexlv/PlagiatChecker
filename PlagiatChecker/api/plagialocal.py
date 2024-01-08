# importation des differents modules 
from difflib import SequenceMatcher 
from pdfminer.high_level import extract_text
import glob
import os


class Plagialocal:
    
    def plagiafichier(self,fichier,fichier2):
        with open(fichier) as first_file, open(fichier2) as second_file: 
            
            # Reading Both Text Files 
            file1 = first_file.read() 
            file2 = second_file.read() 
            
            # Comparing Both Text Files 
            ab = SequenceMatcher(None, file1, 
                                file2).ratio() 
            
            # converting decimal output in integer 
            result = int(ab*100) 
            pourcentage = int(result)
            # Display the final result
            nom1 = os.path.basename(fichier)
            nom = os.path.basename(fichier2)
        
            if pourcentage >= 0 and pourcentage <=25:
                couleur = "badge badge-info"
            elif pourcentage >= 26 and pourcentage <= 50:
                couleur = "badge badge-success"
            elif pourcentage >= 51 and pourcentage <= 74:
                couleur = "badge badge-warning"
            elif pourcentage >= 75 and pourcentage <= 100:
                couleur = "badge badge-danger"
            
            return [nom1,nom,couleur,pourcentage]
        
    
    def plagiapdf(self,fichier,fichier2): 
            #importation du fichier pdf et extraction du texte 
        string1 = extract_text(fichier)
        string2 = extract_text(fichier2)
                
        # Utilisation SequenceMatcher()
        match = SequenceMatcher(None,string1, string2) 
        # convertion du ratio 
        # multiplication par 100 pour avoir le pourcentage
        result = match.ratio() * 100
        pourcentage = int(result)
        # Display the final result
        nom1 = os.path.basename(fichier)
        nom = os.path.basename(fichier2)
        
        if pourcentage >= 0 and pourcentage <=25:
                couleur = "badge badge-info"
        elif pourcentage >= 26 and pourcentage <= 50:
            couleur = "badge badge-success"
        elif pourcentage >= 51 and pourcentage <= 74:
            couleur = "badge badge-warning"
        elif pourcentage >= 75 and pourcentage <= 100:
            couleur = "badge badge-danger"
         
        #return pourcentage   
        return [nom1,nom,couleur,pourcentage]
       
        
        
        def _si_pdf(self,data):
            veri = False
            ref_file=data
            extension=ref_file.split('.')[-1]
            if extension == 'pdf':
                veri = True
            
            return veri
        
       