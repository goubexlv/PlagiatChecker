from django.shortcuts import render
from api.workfile import *
from plagiatOnline.form import DocumentsForm
from plagiatOnline.models import Documents
from api.api_plagiat import * 
from django.http import JsonResponse

# Create your views here.


def plagiatOnline(request):
    return render(request, "online/index.html")

def upload_file(request):
    fichier = str(request.FILES['file'])
    if request.method == 'POST':
        if Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
            doc = DocumentsForm(request.POST,request.FILES)
            resultat = ''
            if doc.is_valid():
                doc.save()
                dernier = Documents.objects.latest('id')
                documents = Documents.objects.all()
                for document in documents:
                    if  str(document.file) != str(dernier.file):
                        resultat = extract_file_content("./media/"+str(dernier.file))
                return JsonResponse({'status': 'success', 'result': resultat })
                
            else:
                return JsonResponse({'status': 'error', 'errors': doc.errors})
        else:
            if Typefile(fichier) == "pdf":
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
        online_plagiarism_checker = PDFContentExtractor()
        result = online_plagiarism_checker.extract_text_from_pdf(pdf_file)
        return {'status': 'success', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def extract_file_content(pdf_file):
    try:
        online_plagiarism_checker = PDFContentExtractor()
        result = online_plagiarism_checker.lire_contenu_fichier(pdf_file)
        return {'status': 'success', 'result': result}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def check_plagiat(request):
    if request.method == "POST":
        try:
            online_plagiarism_checker = OnlinePlagiatChecker()
            text = list(request.POST.keys())[0]
            texting  =  text[:50]
            result = online_plagiarism_checker.check_plagiarism(texting)
            
            return JsonResponse({'status': 'success', 'result': result}, content_type='application/json')  # Assurez-vous de spécifier le bon type de contenu
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
