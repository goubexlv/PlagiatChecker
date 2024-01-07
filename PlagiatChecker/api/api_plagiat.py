import requests
from pdfminer.high_level import extract_text

class OnlinePlagiatChecker:

    def __init__(self):
        self.url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"
        self.headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "d4b76f4d56msh1c10f87d1a4df79p1b6ca1jsnc152fa391328",
            "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
        }

    def check_plagiarism(self, text):
        data = {
            "text": text,
            "language": "en",
            "includeCitations": False,
            "scrapeSources": False
        }
        try:
            response = requests.post(self.url, headers=self.headers, json=data)
            response.raise_for_status()
            result = response.json()
            return result
        except requests.exceptions.RequestException as e:
            # Gérez l'erreur selon les besoins (lancer une exception, logger, etc.)
            print(e)

class PDFContentExtractor:

    def extract_text_from_pdf(self, pdf_path):
        return extract_text(pdf_path)
    
    def lire_contenu_fichier(self,chemin_du_fichier):
        try:
            with open(chemin_du_fichier, 'r') as fichier:
                contenu = fichier.read()
                return contenu
        except FileNotFoundError:
            return f'Le fichier {chemin_du_fichier} n\'existe pas.'
        except Exception as e:
            return f'Une erreur s\'est produite : {str(e)}'
    
# #Exemple d'utilisation
# online_plagiarism_checker = OnlinePlagiatChecker()

# # Extraction du contenu PDF

# # Vérification en ligne du plagiat
# result = online_plagiarism_checker.check_plagiarism("You don't show where you are trying to reverse this URL, but it looks like you have double-quoted it. If you're using the url tag, note that you don't need quotes around the url name:")

# print(result)
