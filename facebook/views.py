from django.shortcuts import render
from . import models
from django.contrib.auth.decorators import login_required
from annoying.functions import get_object_or_None
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
    return render(request,  'facebook/login.html')

@login_required
def home(request):
    return render(request, 'facebook/home.html')


def logout(request, email=None):
    data = request.POST.copy() or None
    email = data['email']
  
    if request.method == 'POST':
        if email is not None:
            user = get_object_or_None(models.User, email=email)
            if user:
                user.status = False
                user.save()
            else:
                pass
    return render(request, 'facebook/login.html')

def save_profile(backend, user, response, *args, **kwargs):
    if backend.name == 'facebook':
        if response:
            name = response['name']
            email = response['email']
            token = response['access_token']

        user = get_object_or_None(models.User, email=email)

        if not user:
            user = models.User(name=name, email=email, token=token)
            user.status = True
            user.save()
        else:
            user.status = True
            user.save()