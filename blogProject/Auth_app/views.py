from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def print_hello(request):
    return HttpResponse("hello I am django first view")


def p_name(request):
    return render(request,'Auth_app/index.html')

@csrf_exempt
def get_all_data(request):
    if request.method == 'GET':
        try:
            all_users=Contact.objects.all() #queryset
            serializer_data=ContactSerializer(all_users,many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)})
        
    if request.method == 'POST':
        try:
            input_Data=json.loads(request.body)
            serializer_data=ContactSerializer(data=input_Data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data Saved Successfully"},status=201)
        except Exception as e:
            return JsonResponse({"error":str(e)},status=500)
        
@csrf_exempt
def single_user_data(request,pk):
    if request.method == 'GET':
        try:
            user_data=Contact.objects.get(pk=pk)
            serializer_data=ContactSerializer(user_data)
            return JsonResponse(serializer_data.data, safe=False)
        except Contact.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
    
    if request.method == 'PUT':
        try:
            user_data=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)
            serializer_data=ContactSerializer(user_data,data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data Updated Successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except Contact.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        
    if request.method == 'PATCH':
        try:
            user_data=Contact.objects.get(pk=pk)
            input_data=json.loads(request.body)
            serializer_data=ContactSerializer(user_data,data=input_data,partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data Updated Successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except Contact.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        
    if request.method == 'DELETE':
        try:
            user_data=Contact.objects.get(pk=pk)
            user_data.delete()
            return JsonResponse({"message":"Data deleted Successfully"},status=204)
        except Contact.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)