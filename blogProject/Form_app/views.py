from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadFormClass
from .models import FileUploader
# Create your views here.

def fileUploadForm(request):
    if request.method =='POST':
        form=FileUploadFormClass(request.POST,request.FILES)
        if form.is_valid():
            # if you are using model form
            # form.save()

            #if you are using normal form 
            file_uploader=FileUploader(name=form.cleaned_data['name'],file=form.cleaned_data['file'])
            file_uploader.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success":False,"error":form.errors})
    else:
        form=FileUploadFormClass()

    return render(request,'Form_app/fileUploadForm.html',{'form':form})
