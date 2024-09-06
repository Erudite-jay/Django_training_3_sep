from django.http import JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.

def login(request):
    if request.session.get('username'):
        return JsonResponse({'success': True,'message':f"Username: {request.session.get('username')} is already  login."})
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user=User.objects.get(username=username)
            if user.password == password:
                request.session.set_expiry(5)
                request.session['username'] = username
                return JsonResponse(
                    {'success': True,"message":"login successful"}
                )
            else:
                return JsonResponse(
                    {'success': False,"message":"Invalid credentials"}
                )
        except User.DoesNotExist:
            return JsonResponse(
                {'success': False,"message":"Invalid credentials"}
            )
    else:
        return render(request, 'Session_app/login.html')