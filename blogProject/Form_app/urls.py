
from . import views
from django.urls import path

urlpatterns = [
 path('file-upload/',views.fileUploadForm, name="fileUpload")
]
