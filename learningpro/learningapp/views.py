from django.shortcuts import render

# Create your views here.

def home(request):
	print("sds")
	return render(request, 'login.html')

def login1(request):
	print("heelosdaf")
	print(request)
	return render(request, 'login.html')