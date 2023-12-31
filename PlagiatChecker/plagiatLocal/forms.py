from django import forms
from plagiatLocal.models import Document
from plagiatLocal.models import Documentverification


class DocumentForm(forms.ModelForm): 
    class Meta:
        model = Document
        fields = "__all__"
        
        
class DocumentvericationForm(forms.ModelForm): 
    class Meta:
        model = Documentverification
        fields = "__all__"
        

