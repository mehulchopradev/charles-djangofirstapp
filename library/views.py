from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse

from library.models import Student, Book

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

def auth(request):
    username = request.POST['username']
    password = request.POST['password']

    l = Student.objects.filter(username=username, password=password)
    if len(l):
        return HttpResponseRedirect(reverse('library:homepage'))
    else:
        return HttpResponseRedirect(reverse('library:loginpage'))

def show_home(request):
    blist = Book.objects.all()
    context = {
        'booklist': blist
    }
    return render(request, 'library/private/home.html', context)

def show_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book
    }

    return render(request, 'library/private/book.html', context)

# ORM
# OOP -> RDBMS
# class(Model) -> Table
# attributes in class -> Columns
# objects -> Rows
