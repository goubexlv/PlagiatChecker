from django.conf.urls.static import static
from PlagiatChecker import settings

from django.contrib import admin
from django.urls import path
from .views import index
from accounts.views import login_user,register_user,logout_user
from plagiatDocuments.views import plagiatDocument, detect_similarity 
from plagiatLocal.views import plagiatLocal, send_fichier , send_fichier2 , plagiatLocalResponse, plagiatLocalResponse1,plagiatlocal
from plagiatDocuments.views import plagiatDocument
from plagiatLocal.views import plagiatLocal, send_fichier , send_fichier2 ,uploadfichier, plagiatLocalResponse, plagiatLocalResponse1,plagiatlocal
from plagiatOnline.views import plagiatOnline,upload_file,check_plagiat


urlpatterns = [
    path("", login_user, name="login_user"),
    path("dashboard/", index, name="index"),
    path("register/", register_user, name="register_user"),
    path("logout/", logout_user, name="logout"),
    path('admin/', admin.site.urls),
    
    # Ekobo et Ferdinand
    path("plagiatDocument/", plagiatDocument, name="plagiatDocument"),
    path('detect_similarity/', detect_similarity, name='detect_similarity'),
    
    # Dimitri et 45 
    path("plagiatLocal/", plagiatLocal ,name="plagiatLocal"),
    path("plagiatlocal/", plagiatlocal ,name="plagiatLocals"),
    path("plagiatLocals/", plagiatLocalResponse ,name="resultat"),
    
    path("uploads/", uploadfichier ,name="uploadfichier"),
    path("send/", send_fichier ,name="envoifichier"),
    path("send2/", send_fichier2 ,name="envoifichier2"),
    
    
    # Gallagher
    path("plagiatOnline/", plagiatOnline ,name="plagiatOnline"),
    path("upload_file/", upload_file ,name="upload_file"),    
    path("check_plagiat/", check_plagiat,name="check_plagiat"),   
    # path("plagiat_detection/", plagiat_detection,name="plagiat_detection"),    
     

]
