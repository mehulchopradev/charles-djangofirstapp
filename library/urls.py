from django.urls import path

from library import views

app_name = 'library'

urlpatterns = [
    # imagine librarymgmt/
    path('index', views.show_login, name='loginpage'),
    path('register', views.show_register, name='registerpage'),
    path('register-user', views.register_user, name='registeruser'),
    path('auth', views.auth, name='authenticate'),
    path('home', views.show_home, name='homepage'),
    path('books/<int:book_id>', views.show_book, name='bookdetails'),
    path('friends', views.get_friends, name='getfriends'),
    path('logout', views.logout, name='logout'),
    path('issue-book/<int:book_id>', views.issue_book, name='issuebook'),
    path('return-book/<int:book_id>', views.return_book, name='returnbook')
]
