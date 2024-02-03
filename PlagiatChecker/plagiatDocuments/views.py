from django.shortcuts import render
from difflib import SequenceMatcher
from django.http import JsonResponse


def plagiatDocument(request):
    return render(request, "documents/index.html")


def plagiat_detection(request):
    try:
        if request.method == 'POST':
            # Obtenez les deux documents à comparer depuis le formulaire
            document1 = request.POST.get('fileFromDropzone1', '')
            document2 = request.POST.get('fileFromDropzone2', '')

            # Calculez le rapport de similarité entre les deux documents
            ratio = SequenceMatcher(None, document1, document2).ratio()

            # Affichez le résultat (à adapter selon vos besoins)
            return JsonResponse ({'ratio': ratio, 'document1': document1, 'document2': document2})
    
    except Exception as e:
        # Gérez l'exception ici (par exemple, en affichant un message d'erreur)
        return render(request, 'error.html', {'error_message': str(e)})
    return render(request, "documents/index.html")
    