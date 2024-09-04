from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
# Create your views here.

def print_hello(request):
    return HttpResponse("hello I am django first view")


def p_name(request):
    return render(request,'Auth_app/index.html')

def get_all_data(request):
    if request.method == 'GET':
        try:
            all_users=Contact.objects.all() #queryset
            serializer_data=ContactSerializer(all_users,many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)})