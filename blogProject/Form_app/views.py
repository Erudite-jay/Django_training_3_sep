from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadFormClass
# Create your views here.

def fileUploadForm(request):
    if request.method =='POST':
        form=FileUploadFormClass(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success":False,"error":form.errors})
    else:
        form=FileUploadFormClass()

    return render(request,'Form_app/fileUploadForm.html',{'form':form})
