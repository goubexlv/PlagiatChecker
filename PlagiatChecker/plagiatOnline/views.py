from django.shortcuts import render

# Create your views here.


def plagiatOnline(request):
    return render(request, "online/index.html")