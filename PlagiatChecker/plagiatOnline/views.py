import pprint
from django.shortcuts import render
from pdfminer.high_level import extract_text
from django.http import HttpResponseRedirect, JsonResponse
from plagiatOnline.form import DocumentsForm
from plagiatOnline.models import Documents
from api.api_plagiat import * 
from django.http import JsonResponse

# Create your views here.


def plagiatOnline(request):
    return render(request, "online/index.html")

def upload_file(request):
    if request.method == 'POST':
        doc = DocumentsForm(request.POST,request.FILES)
        resultat = ''
        if doc.is_valid():
            doc.save()
            dernier = Documents.objects.latest('id')
            documents = Documents.objects.all()
            for document in documents:
                if  str(document.file) != str(dernier.file):
                    resultat = extract_pdf_content("./media/"+str(dernier.file))
            return JsonResponse({'status': 'success', 'result': resultat })
            
        else:
            return JsonResponse({'status': 'error', 'errors': doc.errors})
    else:
        doc = DocumentsForm()

    return JsonResponse({'status': 'error', 'message': 'Method not allowed'})


def extract_pdf_content(pdf_file):
    try:
        online_plagiarism_checker = Onlineplagiat()
        result = online_plagiarism_checker.extraction_contenu_pdf(pdf_file)
        return {'status': 'success', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def check_plagiat(request):
    if request.method == "POST": 
        try:
            online_plagiarism_checker = Onlineplagiat()
            text = request.POST.get('text', '')  # Récupérer le texte de la requête POST
            #print(text)
            result = online_plagiarism_checker.onlineText(text)
            return JsonResponse({'status': 'success', 'result': result})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


