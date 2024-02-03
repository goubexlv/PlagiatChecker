from django.shortcuts import render,redirect
from django.contrib.auth  import get_user_model,login,logout,authenticate
# Create your views here.

user = get_user_model()

def login_user(request):
    if request.method ==  'POST':
        # connecter l'utilisateur
        username =  request.POST.get("username")
        password =  request.POST.get("password")
        
        user = authenticate(username=username , password=password)
        
        if user:
            login(request , user)
            return  redirect('plagiatOnline')
    return render(request,'accounts/login.html')

def register_user(request):
    if request.method == 'POST':
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        
        #Inserer dans la base de donnee 
        user_create =  user.objects.create_user(username=username,
                                                password=password,
                                                first_name=firstname,
                                                last_name=lastname)
        # Ensuite Connecter L'utilisateur inscrit
        login(request, user_create)
        # Et rediriger vers la page d'acceuil
        return redirect('plagiatOnline')
    return render(request, 'accounts/register.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')