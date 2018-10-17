from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse

from library.models import Student

# Create your views here.

def show_login(request):
    return render(request, 'library/public/login.html')

def show_register(request):
    return render(request, 'library/public/register.html')

def register_user(request):
    username = request.POST['username']
    password = request.POST['password']
    country = request.POST['country']

    s = Student(username=username, password=password, country=country)
    s.save()

    if s.id:
        # successfully registered
        return HttpResponseRedirect(reverse('library:loginpage'))
    else:
        return HttpResponse('Error in registration')

# ORM
# OOP -> RDBMS
# class(Model) -> Table
# attributes in class -> Columns
# objects -> Rows
