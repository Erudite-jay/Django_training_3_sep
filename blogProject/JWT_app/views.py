from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            refresh=RefreshToken.for_user(user)
            return JsonResponse({
                "success": True,
                "message": "Login Successful",
                "refresh": str(refresh),
                "access_token": str(refresh.access_token)
                },status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)