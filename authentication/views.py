from django.shortcuts import render
from django.views import View
import  json
from django.http import  JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib import messages
# Create your views here.

class RegistrationView(View): 
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        messages.success(request, 'Success')
        messages.error(request, 'Error')
        messages.warning(request, 'Warning')
        messages.info(request, 'Info')
        return render(request, 'authentication/register.html')


class UsernameValidationView(View): 
    def post(self, request):
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only conatin alphanumeric characters'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'username_error': 'Sorry, username is already taken'}, status=409)
        return JsonResponse({'username_valid': True})
        

class EmailValidationView(View): 
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, email is already taken'}, status=409)
        return JsonResponse({'email_valid': True})
        
