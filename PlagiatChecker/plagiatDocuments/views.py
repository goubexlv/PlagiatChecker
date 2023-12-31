from django.shortcuts import render

# Create your views here.


def plagiatDocument(request):
    return render(request, "documents/index.html")