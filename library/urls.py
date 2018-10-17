from django.urls import path

from library import views

app_name = 'library'

urlpatterns = [
    # imagine librarymgmt/
    path('index', views.show_login, name='loginpage'),
    path('register', views.show_register, name='registerpage'),
    path('register-user', views.register_user, name='registeruser')
]
