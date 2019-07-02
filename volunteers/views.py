from django.shortcuts import render
from django.contrib.auth.form import UserCreationForm
# Create your views here.
def index(request):
    return render(request, 'volunteers/index.html')

def signup(request):
    return render(request, 'volunteers/signup_form.html')

