from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets

# from . import serializers
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
def home(request):
	print("sds")
	return render(request, 'login.html')

def login1(request):
	print("heelosdaf")
	print(request)
	return render(request, 'login.html')

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def rest_login(request):
    print("dsdsd")
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        print("username",username)
        print("password",password)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(86400) #sets the exp. value of the session
                print(request.session.set_expiry(86400))

                rest_login(request, user) #the user is now logged in