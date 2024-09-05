from django import forms
from .models import FileUploader

class FileUploadFormClass(forms.ModelForm):
    class Meta:
        model= FileUploader
        fields = ['name','file']

