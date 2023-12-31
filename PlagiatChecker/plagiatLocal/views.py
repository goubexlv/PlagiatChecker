from django.shortcuts import render, redirect
from plagiatLocal.forms import DocumentForm
from plagiatLocal.models import Document

from api.workfile import *
from api.plagialocal import * 

# Create your views here.


def plagiatLocal(request):
    return render(request, "locale/index.html")


def send_fichier(request):
    fichier = str(request.FILES['nomdoc'])
    pdfverif = []
    plagia = Plagialocal()
    if request.method == 'POST':
        if Typefile(fichier) == "pdf":
            doc = DocumentForm(request.POST,request.FILES)
            if doc.is_valid():
                doc.save()
                
                dernier = Document.objects.latest('id')
                documents = Document.objects.all()
                for document in documents:
                    if Typefile(str(document.nomdoc)) == "pdf" and str(document.nomdoc) != str(dernier.nomdoc):
                        pdfverif.append(plagia.plagiapdf("./media/public/"+fichier,"./media/"+str(document.nomdoc)))
                
            print(pdfverif)
            return redirect("plagiatLocal")                
    

def send_fichier2(request):
    fichier = str(request.FILES['nomdoc'])
    if request.method == 'POST':
        if Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
            doc = DocumentForm(request.POST,request.FILES)
            if doc.is_valid():
                    doc.save()
                    return redirect("plagiatLocal")
    