import requests
from pdfminer.high_level import extract_text


class Onlineplagiat :
    
    def onlineText(self,text):
        url = "https://plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com/plagiarism"
        headers = {
            "Content-Type": "application/json",
            "X-RapidAPI-Key": "0fcccf228bmshab8f84877ac8a36p14fb9ejsn5befbc823f88",
            "X-RapidAPI-Host": "plagiarism-checker-and-auto-citation-generator-multi-lingual.p.rapidapi.com"
        }
        
        data = {
            "text": text,
            "language": "en",
            "includeCitations": False,
            "scrapeSources": False
        }
        try:
            print(text)
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()  
            result = response.json()
            return result
        except requests.exceptions.RequestException as e:
            print(e)
    
    def extraction_contenu_pdf(self,document_a_extraire):
        return extract_text(document_a_extraire)
