
from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse

def main(request):
    return render(request, 'polls/main.html')
def login(request):
    return render(request, 'polls/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'polls/main.html')
