from django import forms
from .models import FileUploader

#model form
# class FileUploadFormClass(forms.ModelForm):
#     class Meta:
#         model= FileUploader
#         fields = ['name','file']

#normal form
class FileUploadFormClass(forms.Form):
  name=forms.CharField(max_length=100)
  file=forms.FileField()