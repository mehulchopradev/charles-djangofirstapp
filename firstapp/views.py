from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def show_home_page(request):
    # return HttpResponse('<html><body><h2>Welcome to my home page</h2></body></html>')
    now = datetime.time(datetime.now())
    hour = now.hour
    if hour >= 0 and hour < 12:
        message = 'Good morning'
    elif hour >= 12 and hour < 16:
        message = 'Good afternoon'
    else:
        message = 'Good evening'

    context = {
        'message': message
    }

    return render(request, 'home.html', context)

def show_contactus(request):
    # imagine email, mobile coming from the database
    email = 'mehul.chopra.dev@yahoo.com'
    mobile = '987907689'
    addresses = [
        {
            'country': 'India',
            'line1': 'Four Bungalows, Mumbai'
        },
        {
            'country': 'USA',
            'line1': 'Texas'
        },
        {
            'country': 'China',
            'line1': 'sdfdslfnd fdk gdfg df'
        }
    ]

    context = {
        'mobile': mobile,
        'email': email,
        'addresses': addresses
    }
    return render(request, 'contactus.html', context)
