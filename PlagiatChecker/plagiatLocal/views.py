from django.shortcuts import render, redirect
from plagiatLocal.forms import DocumentForm
from plagiatLocal.models import Document
from plagiatLocal.models import Rapport
import os.path
from glob import iglob
import os

from api.workfile import *
from api.plagialocal import * 

# Create your views here.
def plagiatlocal(request):
    n = '1'
    context = {
       'errors': n
            }

    return render(request, "locale/index.html", context)

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
    fichier = str(request.FILES['nomdoc'])
    liste_sup = Rapport.objects.all()
    if liste_sup:
        for sup in liste_sup:
            rapp = Rapport.objects.get(id=sup.id)
            rapp.delete()
    
    
    pdfverif = []
    plagia = Plagialocal()
    if Typefile(fichier) == "pdf":
        if request.method == 'POST':
            
                doc = DocumentForm(request.POST,request.FILES)
                if doc.is_valid():
                    doc.save()
                    
                    dernier = Document.objects.latest('id')
                    documents = Document.objects.all()
                    files = listedefichier()
                    ids = 0
                    for file in files:
                        path = './media/'+str(dernier.nomdoc)
                        if file != path:
                            nouveau = []
                            if os.path.isfile(path) :
                                nouveau.append(plagia.plagiapdf('./media/public/'+fichier,file))
                                ids = ids + 1
                                for nv in nouveau:
                                    rapport = Rapport(ids,nv[0],nv[1],nv[2],nv[3],0)
                                    rapport.save()  
                                    pdfverif.append(rapport)
                 
                #return render(request,"locale/result.html",{'n':n},{'resultats': rapport_list}) 
                return redirect("resultat")
    else:
       
        return redirect("plagiatLocals")
        
                                
    

def send_fichier2(request):
    liste_sup = Rapport.objects.all()
    if liste_sup:
        for sup in liste_sup:
            rapp = Rapport.objects.get(id=sup.id)
            rapp.delete()
    
    fichier = str(request.FILES['nomdoc'])
    pdfverif = []
    plagia = Plagialocal()
    if Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
        if request.method == 'POST':
            
                doc = DocumentForm(request.POST,request.FILES)
                if doc.is_valid():
                        doc.save()
                        
                        typf = Typefile(fichier)
                        print(typf)
                        dernier = Document.objects.latest('id')
                        documents = Document.objects.all()
                        files = listedefichiers(typf)
                        ids = 0
                        for file in files:
                            path = './media/'+str(dernier.nomdoc)
                            if file != path:
                                nouveau = []
                                if os.path.isfile(path) :
                                    nouveau.append(plagia.plagiafichier('./media/public/'+fichier,file))
                                    ids = ids + 1
                                    for nv in nouveau:
                                        rapport = Rapport(ids,nv[0],nv[1],nv[2],nv[3],0)
                                        rapport.save()
                                    pdfverif.append(rapport)
                    
                    
                print(pdfverif) 
                rapport_list = Rapport.objects.all()
                n='0'
                context = {
                    'resultats': rapport_list
                }
                return redirect("resultat")
    
    else:
       
        return redirect("plagiatLocals")
                
                    
def uploadfichier(request):
    fichier = str(request.FILES['thefile'])
    if Typefile(fichier) == "pdf" or Typefile(fichier) == "txt" or Typefile(fichier) == "py" or Typefile(fichier) == "c":
        if request.method == 'POST':
            documents = Document.objects.all()
            ids = len(documents) + 1
            doc = Document(ids,'public/'+str(request.FILES['thefile']))
            doc.save()
            upload_file(request.FILES['thefile'])   
                
        return redirect("plagiatLocal")
    else:
        return redirect("plagiatLocals")
    