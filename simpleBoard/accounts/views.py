from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


def signup(request):
    return render(request,'accounts/signup.html')


def createUser(request):
    id = request.POST['id']
    pw = request.POST['pw']
    user = User(username=id, password=make_password(pw))
    user.save()

    return HttpResponseRedirect(reverse('list'))