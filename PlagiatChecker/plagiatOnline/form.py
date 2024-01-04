from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()


from django import forms
from plagiatOnline.models import Documents


class DocumentsForm(forms.ModelForm): 
    class Meta:
        model = Documents
        fields = "__all__"
        