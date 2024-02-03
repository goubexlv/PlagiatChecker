from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
#from PIL import Image
import spacy
import os
import hashlib
import chardet
#import fitz
#import pytesseract
# Create your views here.


def plagiatDocument(request):
    return render(request, "documents/index.html")

# Charger le modèle SpaCy pour le traitement du langage naturel
nlp = spacy.load("en_core_web_sm")

def calculate_similarity(doc1, doc2):
    """
    Calculer la similarité entre deux objets Doc.
    """
    return doc1.similarity(doc2)

def calculate_file_hash(file_content):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(file_content)
    return sha256_hash.hexdigest()

def jaccard_similarity(hash1, hash2):
    set1 = set(hash1)
    set2 = set(hash2)
    intersection = len(set1.intersection(set2))
    union = len(set1) + len(set2) - intersection
    return intersection / union if union != 0 else 0

# def extract_text_from_pdf(file):
#     """
#     Extract text from a PDF file using PyMuPDF.
#     """
#     try:
#         doc = fitz.open(file)
#         text = ""
#         for page_num in range(doc.page_count):
#             page = doc[page_num]
#             image_list = page.get_images(full=True)
#             for img_index, img_info in enumerate(image_list):
#                 img = page.get_image(img_info)
#                 base_image = Image.frombytes("RGB", [img.width, img.height], img.samples)
#                 text += pytesseract.image_to_string(base_image)
#             text += page.get_text()
#         return text
#     except Exception as e:
#         print(f"Error extracting text from PDF with OCR: {e}")
#         return ""

def detect_similarity(request):
    result_message = ""
    if request.method == 'POST':
        document1 = request.FILES.get('file1', None)
        document2 = request.FILES.get('file2', None)

        if not document1 or not document2:
            return JsonResponse({'error': 'Veuillez sélectionner deux fichiers non vides.'}, status=400)


        ext1 = document1.name.split('.')[-1].lower()
        ext2 = document2.name.split('.')[-1].lower()

        if ext1 != ext2:
            return JsonResponse({'error': 'Les fichiers doivent avoir la même extension.'}, status=400)

        content1 = document1.read()
        content2 = document2.read()
        try:
            encoding1 = chardet.detect(content1)['encoding']
            encoding2 = chardet.detect(content2)['encoding']

        # Décoder le contenu en UTF-8 en utilisant l'encodage détecté
            decoded_content1 = content1.decode(encoding1)
            decoded_content2 = content2.decode(encoding2)
        except TypeError:
            # En cas d'échec de la détection d'encodage, utilisez UTF-8 par défaut, gallager c'est high je te jure.
            decoded_content1 = content1.decode('utf-8', errors='ignore')
            decoded_content2 = content2.decode('utf-8', errors='ignore')

        # Appliquer le traitement NLP aux documents
        doc1 = nlp(decoded_content1)
        doc2 = nlp(decoded_content2)

        # Calculer la similarité entre les documents avec SpaCy (valeur entre 0 et 1)
        spacy_similarity_score = calculate_similarity(doc1, doc2)

        hash1 = calculate_file_hash(decoded_content1.encode('utf-8'))
        hash2 = calculate_file_hash(decoded_content2.encode('utf-8'))
        jaccard_similarity_score = jaccard_similarity(hash1, hash2) * 100
        # hash1 = calculate_file_hash(document1.read())
        # hash2 = calculate_file_hash(document2.read())

        # Calculer la similarité de Jaccard
        

        # Comparer les hachages
        if hash1 == hash2:
            result_message = 'Les fichiers sont similaires.'
            return render(request, 'similarity_result.html', {
            'spacy_similarity_percentage': round(spacy_similarity_score * 100, 2),
            'jaccard_similarity_percentage': round(jaccard_similarity_score, 2),
        })
        #     return JsonResponse({
        #     'resultat': 'Les fichiers sont similaires.',
        #     'spacy_similarity_percentage': round(spacy_similarity_score * 100, 2),
        #     'jaccard_similarity_percentage': round(jaccard_similarity_score, 2)
        # })
        else:
            result_message = 'Les fichiers sont différents.'
            return render(request, 'similarity_result.html', {
            'spacy_similarity_percentage': round(spacy_similarity_score * 100, 2),
            'jaccard_similarity_percentage': round(jaccard_similarity_score, 2),
        })
        #     return JsonResponse({
        #     'resultat': 'Les fichiers sont différents.',
        #     'spacy_similarity_percentage': round(spacy_similarity_score * 100, 2),
        #     'jaccard_similarity_percentage': round(jaccard_similarity_score, 2)
        # })

    # Rendre le modèle avec le résultat de la comparaison
        
        

    # Renvoyer une réponse par défaut si la requête n'est pas de type POST
    return JsonResponse({'error': 'Méthode non autorisée.'}, status=405)
        # Lire le contenu des fichiers
        # content1 = ""
        # content2 = ""

        # if ext1 == ".pdf":
        #     content1 = extract_text_from_pdf(document1)
        # else:
        #     content1 = document1.read().decode('utf-8')

        # if ext2 == ".pdf":
        #     content2 = extract_text_from_pdf(document2)
        # else:
        #     content2 = document2.read().decode('utf-8')

        # Appliquer le traitement NLP aux documents
        # doc1 = nlp(content1)
        # doc2 = nlp(content2)

        # Calculer la similarité entre les documents (valeur entre 0 et 1)
        # similarity_score = doc1.similarity(doc2)
        # similarity_percentage = round(similarity_score * 100, 2)
        # seuil_similitude = 0.85

        # Comparer le score de similitude avec le seuil
        # if similarity_score >= seuil_similitude:
            # Les documents sont similaires
            #  return JsonResponse({'result': 'Les fichiers sont similaires.', 'similarity_score': similarity_score,'soit en pourcentage': similarity_percentage})
           
            # return render(request, 'similarity_result.html', {'similarity_score': similarity_percentage, 'result_message': result_message})
        # else:
            
            # Les documents sont différents
            # return JsonResponse({'result': 'Les fichiers sont différents.', 'similarity_score': similarity_score,'soit en pourcentage': similarity_percentage})

    # return render(request, 'similarity_result.html', {'similarity_score': similarity_percentage, 'result_message': result_message})

  