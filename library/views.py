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
        # remember the username data
        request.session['username'] = username
        request.session['id'] = l[0].id
        # request.session['student'] = l[0]
        return HttpResponseRedirect(reverse('library:homepage'))
    else:
        return HttpResponseRedirect(reverse('library:loginpage'))

def show_home(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:loginpage'))

    # retrieve the data (username) from the session
    username = request.session['username']
    studentid = request.session['id']
    blist = Book.objects.exclude(count=0)
    for book in blist:
        students = book.student_set.filter(pk=studentid)
        if len(students):
            book.alreadyissued = True
        else:
            book.alreadyissued = False

        studentsissued = book.student_set.count()
        if book.count - studentsissued == 0:
            book.canbeissued = False
        else:
            book.canbeissued = True

    context = {
        'booklist': blist,
        'username': username
    }
    return render(request, 'library/private/home.html', context)

def show_book(request, book_id):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:loginpage'))

    # retrieve the data (username) from the session
    username = request.session['username']
    book = Book.objects.get(pk=book_id)
    context = {
        'book': book,
        'username': username
    }

    return render(request, 'library/private/book.html', context)

def get_friends(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:loginpage'))

    username = request.session['username']
    studentid = request.session['id']
    students = Student.objects.exclude(pk=studentid)
    context = {
        'friends': students,
        'username': username
    }

    return render(request, 'library/private/friends.html', context)

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('library:loginpage'))

def issue_book(request, book_id):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:loginpage'))

    studentid = request.session['id']

    student = Student.objects.get(pk=studentid)
    book = Book.objects.get(pk=book_id)

    student.books_issued.add(book)

    return HttpResponseRedirect(reverse('library:homepage'))

def return_book(request, book_id):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:loginpage'))

    studentid = request.session['id']
    student = Student.objects.get(pk=studentid)
    student.books_issued.remove(book_id)

    return HttpResponseRedirect(reverse('library:homepage'))

# ORM
# OOP -> RDBMS
# class(Model) -> Table
# attributes in class -> Columns
# objects -> Rows
