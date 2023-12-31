from django.shortcuts import render, redirect
from plagiatLocal.forms import DocumentForm
from plagiatLocal.models import Document
from plagiatLocal.models import Rapport

from api.workfile import *
from api.plagialocal import * 

# Create your views here.


def plagiatLocal(request):

    return render(request, "locale/index.html")

def plagiatLocalResponse(request):
    rapport_list = Rapport.objects.all()
    n='0'
    context = {
                'resultats': rapport_list
    
            }
    return render(request, "locale/results.html",context)

def plagiatLocalResponse1(request):
    rapport_list = Rapport.objects.all()
    n='0'
    context = {
                'resultats': rapport_list
    
            }
    return render(request, "locale/resultss.html",context)


def send_fichier(request):
    liste_sup = Rapport.objects.all()
    if liste_sup:
        for sup in liste_sup:
            rapp = Rapport.objects.get(id=sup.id)
            rapp.delete()
    
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
                        nouveau = []
                        nouveau.append(plagia.plagiapdf("./media/public/"+fichier,"./media/"+str(document.nomdoc)))
                        for nv in nouveau:
                            rapport = Rapport(document.id,nv[0],nv[1],nv[2],nv[3],0)
                            rapport.save()
                        pdfverif.append(rapport)
            
            
            print(pdfverif) 
            rapport_list = Rapport.objects.all()
            n='0'
            context = {
                'resultats': rapport_list
            }
            #return render(request,"locale/result.html",{'n':n},{'resultats': rapport_list}) 
            return redirect("resultat")
                                
    

def send_fichier2(request):
    liste_sup = Rapport.objects.all()
    if liste_sup:
        for sup in liste_sup:
            rapp = Rapport.objects.get(id=sup.id)
            rapp.delete()
    
    fichier = str(request.FILES['nomdoc'])
    pdfverif = []
    plagia = Plagialocal()
    if request.method == 'POST':
        if Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
            doc = DocumentForm(request.POST,request.FILES)
            if doc.is_valid():
                    doc.save()
                    
                    typf = Typefile(fichier)
                    dernier = Document.objects.latest('id')
                    documents = Document.objects.all()
                    for document in documents:
                        if Typefile(str(document.nomdoc)) == typf and str(document.nomdoc) != str(dernier.nomdoc):
                            nouveau = []
                            nouveau.append(plagia.plagiafichier("./media/public/"+fichier,"./media/"+str(document.nomdoc)))
                            for nv in nouveau:
                                rapport = Rapport(document.id,nv[0],nv[1],nv[2],nv[3],0)
                                rapport.save()
                            pdfverif.append(rapport)
                
                
            print(pdfverif) 
            rapport_list = Rapport.objects.all()
            n='0'
            context = {
                'resultats': rapport_list
            }
            return redirect("resultat")
                
                    
    